import yaml

CONF_API_KEY = '6c1969c41f17400213c51a6d0b0fbad9'
CONF_LATITUDE = 50
CONF_LONGITUDE = 50


new_data = f"""
openweathermap_current: http://api.openweathermap.org/data/2.5/air_pollution?lat={CONF_LATITUDE}&lon={CONF_LONGITUDE}&appid={CONF_API_KEY}
openweathermap_forecast: http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={CONF_LATITUDE}&lon={CONF_LONGITUDE}&appid={CONF_API_KEY}
sensor:
  #Open Weather Map - Air Pollution API - Forecast Report
  - platform: rest
    name: "Openweathermap Forecast: Air Pollution"
    scan_interval: 3600
    resource: !secret openweathermap_forecast
    value_template: 'OK'
    json_attributes_path: "$.list[0]"
    json_attributes:
      - dt
      - main
      - components
  - platform: template
    sensors:
      openweathermap_forecast_air_pollution_forecast_date:
        friendly_name: "Date"
        unique_id: openweathermap_forecast_air_pollution_forecast_date
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'dt') | timestamp_custom('%Y-%m-%d') }}"
        device_class: "date"
      openweathermap_forecast_air_quality_index:
        friendly_name: "Air Quality Index"
        unique_id: openweathermap_forecast_air_quality_index
        device_class: "aqi"
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'main')['aqi'] }}"
      openweathermap_forecast_carbon_monoxide:
        friendly_name: "Carbon Monoxide CO"
        unique_id: openweathermap_forecast_carbon_monoxide
        device_class: "carbon_monoxide"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ '%.2f' | format(state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['co'] / 100) }}"
      openweathermap_forecast_nitrogen_monoxide:
        friendly_name: "Nitrogen Monoxide NO"
        unique_id: openweathermap_forecast_nitrogen_monoxide
        device_class: "nitrogen_monoxide"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['no'] }}"
      openweathermap_forecast_nitrogen_dioxide:
        friendly_name: "Nitrogen Dioxide NO2"
        unique_id: openweathermap_forecast_nitrogen_dioxide
        device_class: "nitrogen_dioxide"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['no2'] }}"
      openweathermap_forecast_ozone:
        friendly_name: "Ozone O3"
        unique_id: openweathermap_forecast_ozone
        device_class: "ozone"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['o3'] }}"
      openweathermap_forecast_sulfur_dioxide:
        friendly_name: "Sulfur Dioxide SO2"
        unique_id: openweathermap_forecast_sulfur_dioxide
        device_class: "sulphur_dioxide"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['so2'] }}"
      openweathermap_forecast_particulate_matter_2_5:
        friendly_name: "PM 2.5"
        unique_id: openweathermap_forecast_particulate_matter_2_5
        device_class: "pm25"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['pm2_5'] }}"
      openweathermap_forecast_particulate_matter_10:
        friendly_name: "PM 10"
        unique_id: openweathermap_forecast_particulate_matter_10
        device_class: "pm10"
        unit_of_measurement: 'µg/m³'
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['pm10'] }}"
      openweathermap_forecast_ammonia:
        friendly_name: "Ammonia NH3"
        unique_id: openweathermap_forecast_ammonia
        unit_of_measurement: 'µg/m³'
        icon_template: mdi:molecule
        value_template: "{{ state_attr('sensor.openweathermap_forecast_air_pollution', 'components')['nh3'] }}"
"""

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def merge_yaml_data(existing_data, new_data):
    existing_data.update(new_data)

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

yaml_file_path = '../../../config/configuration.yaml'
existing_data = read_yaml_file(yaml_file_path)
merge_yaml_data(existing_data, new_data)
write_yaml_file(yaml_file_path, existing_data)
