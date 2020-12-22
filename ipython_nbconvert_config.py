c = get_config()

# Export paper.ipynb to pdf.
c.NbConvertApp.notebooks = ['paper.ipynb']
c.NbConvertApp.export_format = 'pdf'

# Configure our tag removal
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)

# Configure and run out exporter
c.HTMLExporter.preprocessors = ["TagRemovePreprocessor"]

c.Exporter.template_file = 'paper_template'
