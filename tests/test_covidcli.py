from covidcli import __version__
# from click.testing import CliRunner



def test_version():
    assert __version__ == '0.1.7'




# # Test For CLI
# def test_latest_cases():
# 	runner = CliRunner()
# 	result = runner.invoke(main['get latest'])
# 	assert result.output != None
# 	assert result.exit_code == 0 
