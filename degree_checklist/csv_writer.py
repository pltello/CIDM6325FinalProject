import csv
from models import (Student, Degree, Core_Requirements,
                    University_Requirements, Department_Requirements,
                    Major_Requirements, UploadFormModel)


def write_csv(filename, header, data):
    """Write the provided data to the CSV file.

    :param str filename: The name of the file to which the data should be written
    :param list header: The header for the columns in csv file
    :param list data: The list of list mapping the values to the columns
    """
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("Unable to write the contents to csv file. Exception: {}".format(
            csv_file_error))


if __name__ == '__main__':
    header = ['DegreeName', 'DegreeYear',
              'UniversityName', 'DepartmentName', 'MajorName']
    data = [Degree.objects.all().order_by('DegreeName').values()]
    filename = 'degree_list.csv'
    write_csv(filename, header, data)
