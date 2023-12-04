import plotly.express as px
from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements)


def generate_bar_plot(x_axis, y_axis):
    """Generate a bar plot for the provided x and y-axis values."""
    figure = px.bar(x=x_axis, y=y_axis,
                    title="Plot of Current Records by Type")
    return plot(figure, output_type='div')


def generate_html(plot_html):
    """Generate an HTML page for the provided plot."""
    html_content = "<html><head><title>Plot of Current Records by Type</title></head><body>{}</body></html>".format(
        plot_html)
    try:
        with open('plot_demo.html', 'w') as plot_file:
            plot_file.write(html_content)
    except (IOError, OSError) as file_io_error:
        print("Unable to generate plot file. Exception: {}".format(file_io_error))


a = len(Student.objects.all().values())
b = len(Degree.objects.all().values())
c = len(Core_Requirements.objects.all().values())
d = len(University_Requirements.objects.all().values())
e = len(Department_Requirements.objects.all().values())
f = len(Major_Requirements.objects.all().values())

if __name__ == '__main__':
    x = ["Student", "Degree", "Core Requirements", "University Requirements",
         "Department Requirements", "Major Requirements"]
    y = [a, b, c, d, e, f]
    plot_html = generate_bar_plot(x, y)
    generate_html(plot_html)
