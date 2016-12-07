import pandas as pd
import click

@click.command()
@click.option('--input_path', prompt='Input .dta file',  help='Input .dta file')
@click.option('--output_path', prompt='CSV for output', help='The path to csv to create.')
def convert(input_path, output_path):
  input_path = input_path.strip() if input_path else input_path
  output_path = output_path.strip() if output_path else output_path
  data = pd.io.stata.read_stata(input_path)
  data.to_csv(output_path)


if __name__ == '__main__':
  convert()

