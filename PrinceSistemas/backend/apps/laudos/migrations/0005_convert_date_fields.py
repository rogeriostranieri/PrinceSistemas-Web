from django.db import migrations
from datetime import datetime, timedelta
import re

def convert_string_dates(apps, schema_editor):
    Laudo = apps.get_model('laudos', 'Laudo')
    # Regex patterns for various date formats
    date_pattern = r'^\d{2}/\d{2}/\d{4}$'
    datetime_pattern = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'
    trailing_colon_pattern = r'^\d{2}/\d{2}/\d{4}\s*:\s*$'
    iso_date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    iso_datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    iso_datetime_tz_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\+\d{2}(?::\d{2})?)?$'
    empty_pattern = r'^\s*/\s*/\s*(:\s*)?$'

    for laudo in Laudo.objects.all().iterator():  # Use iterator for memory efficiency
        # Date fields (DD/MM/YYYY)
        date_fields = [
            'bombeiros_venc', 'ambiental_venc', 'viabilidade_vec', 'sanitario_venc',
            'setran_venc', 'bombeiro_data_provisorio', 'ambiental_data_provisorio',
            'viabilidade_data_provisorio', 'sanitario_data_provisorio', 'setran_data_provisorio',
            'bombeiro_data_ped_processo', 'bombeiro_data_multa',
            'bombeiro_provisorio_data', 'ambiental_provisorio_data', 'viabilidade_provisorio_data',
            'sanitario_provisorio_data', 'setran_provisorio_data'
        ]
        for field in date_fields:
            value = getattr(laudo, field)
            if value and isinstance(value, str):
                value = value.strip()
                if not value or re.match(empty_pattern, value):
                    setattr(laudo, field, None)
                    print(f"Set {field} to None for laudo {laudo.id_laudos}: empty or malformed ({value})")
                else:
                    try:
                        if re.match(date_pattern, value):
                            # Already in DD/MM/YYYY
                            setattr(laudo, field, value)
                        elif re.match(datetime_pattern, value):
                            # Convert DD/MM/YYYY HH:mm to DD/MM/YYYY
                            dt = datetime.strptime(value, '%d/%m/%Y %H:%M')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y')}")
                        elif re.match(iso_date_pattern, value):
                            dt = datetime.strptime(value, '%Y-%m-%d')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y')}")
                        elif re.match(iso_datetime_pattern, value) or re.match(iso_datetime_tz_pattern, value):
                            # Handle both YYYY-MM-DD HH:MM:SS and YYYY-MM-DD HH:MM:SS+HH:MM
                            clean_value = value.split('+')[0].strip()
                            dt = datetime.strptime(clean_value, '%Y-%m-%d %H:%M:%S')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y')}")
                        elif re.match(trailing_colon_pattern, value):
                            clean_value = value.strip(' :')
                            dt = datetime.strptime(clean_value, '%d/%m/%Y')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y')}")
                        else:
                            setattr(laudo, field, None)
                            print(f"Invalid date in {field} for laudo {laudo.id_laudos}: {value}")
                    except ValueError as e:
                        setattr(laudo, field, None)
                        print(f"Error parsing date in {field} for laudo {laudo.id_laudos}: {value} ({str(e)})")
            elif value and not isinstance(value, str):
                # Handle non-string values (e.g., datetime objects)
                try:
                    dt = value
                    setattr(laudo, field, dt.strftime('%d/%m/%Y'))
                    print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y')}")
                except AttributeError:
                    setattr(laudo, field, None)
                    print(f"Invalid non-string date in {field} for laudo {laudo.id_laudos}: {value}")

        # Date-time fields (DD/MM/YYYY HH:mm)
        datetime_fields = ['data_criado', 'data_entrada']
        for field in datetime_fields:
            value = getattr(laudo, field)
            if value and isinstance(value, str):
                value = value.strip()
                if not value or re.match(empty_pattern, value):
                    setattr(laudo, field, None)
                    print(f"Set {field} to None for laudo {laudo.id_laudos}: empty or malformed ({value})")
                else:
                    try:
                        if re.match(datetime_pattern, value):
                            # Already in DD/MM/YYYY HH:mm
                            setattr(laudo, field, value)
                        elif re.match(date_pattern, value):
                            # Treat as date, add 00:00
                            dt = datetime.strptime(value, '%d/%m/%Y')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y 00:00'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y 00:00')}")
                        elif re.match(iso_date_pattern, value):
                            dt = datetime.strptime(value, '%Y-%m-%d')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y 00:00'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y 00:00')}")
                        elif re.match(iso_datetime_pattern, value) or re.match(iso_datetime_tz_pattern, value):
                            clean_value = value.split('+')[0].strip()
                            dt = datetime.strptime(clean_value, '%Y-%m-%d %H:%M:%S')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y %H:%M'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y %H:%M')}")
                        elif re.match(trailing_colon_pattern, value):
                            clean_value = value.strip(' :')
                            dt = datetime.strptime(clean_value, '%d/%m/%Y')
                            setattr(laudo, field, dt.strftime('%d/%m/%Y 00:00'))
                            print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y 00:00')}")
                        elif '24:' in value:
                            date_part, time_part = value.split(' ')
                            if time_part.startswith('24:'):
                                time_part = '00:' + time_part[3:]
                                dt = datetime.strptime(f"{date_part} {time_part}", '%d/%m/%Y %H:%M')
                                dt += timedelta(days=1)
                                setattr(laudo, field, dt.strftime('%d/%m/%Y %H:%M'))
                                print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y %H:%M')}")
                            else:
                                raise ValueError(f"Invalid time format: {value}")
                        else:
                            setattr(laudo, field, None)
                            print(f"Invalid date-time in {field} for laudo {laudo.id_laudos}: {value}")
                    except ValueError as e:
                        setattr(laudo, field, None)
                        print(f"Error parsing date-time in {field} for laudo {laudo.id_laudos}: {value} ({str(e)})")
            elif value and not isinstance(value, str):
                # Handle non-string values (e.g., datetime objects)
                try:
                    dt = value
                    setattr(laudo, field, dt.strftime('%d/%m/%Y %H:%M'))
                    print(f"Converted {field} for laudo {laudo.id_laudos}: {value} -> {dt.strftime('%d/%m/%Y %H:%M')}")
                except AttributeError:
                    setattr(laudo, field, None)
                    print(f"Invalid non-string date-time in {field} for laudo {laudo.id_laudos}: {value}")

        laudo.save()

class Migration(migrations.Migration):
    dependencies = [
        ('laudos', '0004_alter_laudo_options'),
    ]
    operations = [
        migrations.RunPython(convert_string_dates),
    ]