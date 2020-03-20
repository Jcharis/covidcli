#!/usr/bin/python
import click
import pandas as pd
import datetime
import time
import os

timestr = time.strftime("%Y%m%d-%H%M%S")
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from pyfiglet import Figlet


# DEFAULT URLS FOR DATASOURCE
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
recovered_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
death_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
previous_cases_url = "https://raw.githubusercontent.com/Jcharis/covidcli/master/covidcli/data/coronavirus_dataset.csv"

def get_n_melt_data(data_url, case_type):
    df = pd.read_csv(data_url)
    melted_df = df.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"])
    melted_df.rename(columns={"variable": "Date", "value": case_type}, inplace=True)
    return melted_df


def merge_data(confirm_df, recovered_df, deaths_df):
    new_df = confirm_df.join(recovered_df["Recovered"]).join(deaths_df["Deaths"])
    return new_df


confirm_df = get_n_melt_data(confirmed_cases_url, "Confirmed")
recovered_df = get_n_melt_data(recovered_cases_url, "Recovered")
deaths_df = get_n_melt_data(death_cases_url, "Deaths")


@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan"
)
@click.version_option("0.1.3", prog_name="covidcli")
def main():
    """Covid-cli : A simple CLI for Getting info about Coronavirus Outbreak"""
    pass


@main.command()
@click.argument("cases", type=click.Choice(["confirmed", "recovered", "deaths", "all"]))
def show(cases):
    """Show Cases of Coronavirus by Confirmed|Recovered|Deaths|Previous|Latest"""
    click.secho("Showing:: {} cases".format(cases), bg="blue")
    click.echo("===========================================")
    if cases == "confirmed":
        click.secho(
            "Number of Confirmed Cases:: {}".format(confirm_df["Confirmed"].sum())
        )
        click.echo(confirm_df)
    elif cases == "recovered":
        click.secho(
            "Number of Confirmed Cases:: {}".format(recovered_df["Recovered"].sum())
        )
        click.echo(recovered_df)
    elif cases == "deaths":
        click.secho("Number of Confirmed Cases:: {}".format(deaths_df["Deaths"].sum()))
        click.echo(deaths_df)
    elif cases == "all":
        df = merge_data(confirm_df, recovered_df, deaths_df)
        click.echo(df.tail(20).to_markdown())


@main.group()
def get():
    """Get Info of cases by latest|previous|status|dataset"""
    pass


@get.command("latest")
def get_latest():
    """Get Latest Cases
    
    eg. covidcli get latest

    """
    click.echo("Showing Latest Cases")
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("=============================")
    df = merge_data(confirm_df, recovered_df, deaths_df)
    # df.to_csv("coronavirus_dataset.csv", index=False)
    total_confirmed = df["Confirmed"].sum()
    total_recovered = df["Recovered"].sum()
    total_deaths = df["Deaths"].sum()
    stats_dict = {
        "Confirmed Cases": total_confirmed,
        "Recovered Cases": total_recovered,
        "Death Cases": total_deaths,
    }
    click.echo(stats_dict)


@get.command("previous")
def get_previous():
    """Get Previous Cases (uses yesterdays dataset)
    
    eg. covidcli get previous

    """
    click.echo("Showing Previous Cases")
    click.echo("=============================")
    prev_df = pd.read_csv(previous_cases_url)
    total_confirmed = prev_df["Confirmed"].sum()
    total_recovered = prev_df["Recovered"].sum()
    total_deaths = prev_df["Deaths"].sum()
    stats_dict = {
        "Confirmed Cases": total_confirmed,
        "Recovered Cases": total_recovered,
        "Death Cases": total_deaths,
    }
    click.echo(stats_dict)


@get.command("status")
@click.argument("countryname")
def get_status(countryname):
    """ Get Status of Cases By Country
    
    eg. covidcli get status "Ghana"

    """
    click.echo("Get Status of Cases")
    click.echo(click.style("Country::", fg="blue") + "{}".format(countryname))
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("=============================")
    new_df = merge_data(confirm_df, recovered_df, deaths_df)
    single_country_df = new_df[new_df["Country/Region"] == countryname]
    total_confirmed = single_country_df["Confirmed"].sum()
    total_recovered = single_country_df["Recovered"].sum()
    total_deaths = single_country_df["Deaths"].sum()
    stats_dict = {
        "Confirmed Cases": total_confirmed,
        "Recovered Cases": total_recovered,
        "Death Cases": total_deaths,
    }
    click.echo(stats_dict)


@get.command("dataset")
def get_dataset():
    """Get Dataset or Download dataset
    
    eg. covidcli get dataset

    """
    click.echo("Fetching Dataset")
    click.echo(
        click.style("Accessed Time::", fg="blue") + "{}".format(datetime.datetime.now())
    )
    click.echo("=============================")
    current_df = merge_data(confirm_df, recovered_df, deaths_df)
    click.echo(current_df.tail(20).to_markdown())
    file_name = "coronavirus_dataset_{}.csv".format(timestr)
    current_df.to_csv(file_name, index=False)
    click.secho(
        "Finished Saving Dataset as {}".format(file_name), fg="white", bg="blue"
    )


@main.command()
@click.argument("countryname")
@click.option(
    "--cases",
    "-c",
    help="Specify the Cases Type",
    type=click.Choice(["confirmed", "recovered", "deaths", "previous", "latest"]),
    default="latest",
)
def search(countryname, cases):
    """Search Info about Country

	eg covidcli search "CountryName" --cases confirmed 

	"""
    click.echo(click.style("Searched::", fg="blue") + "{}".format(countryname))
    click.echo("===================================")
    df = merge_data(confirm_df, recovered_df, deaths_df)
    country_df = df[df["Country/Region"] == countryname]
    if cases == "confirmed":
        total_confirmed = country_df["Confirmed"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_confirmed
            )
        )
    elif cases == "recovered":
        total_recovered = country_df["Recovered"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_recovered
            )
        )
    elif cases == "deaths":
        total_deaths = country_df["Deaths"].sum()
        click.echo(
            click.style("Accessed Time:: ", fg="blue")
            + "{}".format(datetime.datetime.now())
        )
        click.echo(
            "Total Number of {} Cases for {}::{}".format(
                cases, countryname, total_deaths
            )
        )
    elif cases == "previous":
        prev_df = pd.read_csv(previous_cases_url)
        prev_country_df = prev_df[prev_df["Country/Region"] == countryname]
        click.echo("Showing Previous Data")
        click.echo(prev_country_df)
    elif cases == "latest":
        current_df = merge_data(confirm_df, recovered_df, deaths_df)
        current_country_df = current_df[current_df["Country/Region"] == countryname]
        click.echo("Showing Latest Data")
        click.echo(current_country_df)
    else:
        click.echo(country_df)


@main.command()
def info():
    """Info About CLI """
    f = Figlet(font='standard')
    click.echo(f.renderText('Covid-cli'))
    click.secho("covidcli: a simple CLI for tracking Coronavirus Outbreak",fg='cyan')
    click.echo("Source of Data: John Hopkins ")
    click.secho("Jesus Saves@JCharisTech",fg='cyan')
    click.echo("By: Jesse E.Agbe(JCharis)")


if __name__ == "__main__":
    main()
