import os
import logging

SYSTEM_ROOT =  os.path.dirname(os.path.realpath(__file__))
# BULK_PATENT_REPOSITORY_DIRECTORY = "bulk_patent"

# if os.path.isfile(filename):
#
#     xml_document_list = []
#
#     with open(fname, 'r') as f:
#         op = ''
#         cntr = 1
#         find1 = "xml"
#         start = 0
#         for line in f:
#             #if start == 1:
#             if find1 in line:
#                 xml_document_list = []
#                 xml_document_list.append(line)
#                 if start==1:
#                     # op += find1
#                     with open('{0}pat1.txt'.format(str(cntr)), 'w') as opf:
#                         opf.write(op)
#                         opf.close()
#                         op=''
#                         cntr=cntr+1
#                 else:
#                     start=1
#             else:
#                 xml_document_list.append(line)
#                 op+= line
#
#
#             print(op)
#         f.close()



def get_full_patent_content_list(target_dir):
    try:
        with open(target_dir, 'r') as f:
            return f.readlines()
    except FileExistsError as e:
        logging.error("File Not Exists: " + target_dir)
        logging.error(e)


def get_patent_start_address(full_document):
    return [index for index, line in enumerate(full_document) if '''xml version="1.0"''' in line]


def get_patent_document_list(filename):
    target_file = os.path.join(SYSTEM_ROOT, filename)
    full_document_list = get_full_patent_content_list(target_file)
    logging.info("Get full document list from " + target_file)

    start_index_list = get_patent_start_address(full_document_list)

    prior = 0
    patent_document_list = []
    for start_index in start_index_list[1:]:
        patent_document_list.append("".join(full_document_list[prior: int(start_index)]))
        prior = start_index
    else:
        patent_document_list.append("".join(full_document_list[prior:]))
    print(patent_document_list)
    logging.info("Get document number of documents :" + str(len(patent_document_list)))

    return patent_document_list

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p')
    filename = "samplepatent.txt"
    patent_codocuments = get_patent_document_list(filename)


