from covidcli import __version__
# from click.testing import CliRunner

from covidcli.covidcli import main,get_n_melt_data,merge_data


# DEFAULT URLS FOR DATASOURCE Modified
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
recovered_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
death_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
previous_cases_url = "https://raw.githubusercontent.com/Jcharis/covidcli/master/covidcli/data/coronavirus_dataset.csv"

confirm_df = get_n_melt_data(confirmed_cases_url, "Confirmed")
recovered_df = get_n_melt_data(recovered_cases_url, "Recovered")
deaths_df = get_n_melt_data(death_cases_url, "Deaths")

def test_version():
    assert __version__ == '0.1.6'

def test_data_received_from_url():
	df = merge_data(confirm_df, recovered_df, deaths_df)
	assert isinstance(df,type(df))


# # Test For CLI
# def test_latest_cases():
# 	runner = CliRunner()
# 	result = runner.invoke(main['get latest'])
# 	assert result.output != None
# 	assert result.exit_code == 0 
