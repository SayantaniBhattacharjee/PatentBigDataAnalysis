import os
fname = "C:\\Users\\Tanima Sarbajna\\PycharmProjects\\untitled\\samplepatent.txt"
if os.path.isfile(fname):

    xml_document_list = []

    with open(fname, 'r') as f:
        op = ''
        cntr = 1
        find1 = "xml"
        start = 0
        for line in f:
            #if start == 1:
            if find1 in line:
                xml_document_list = []
                xml_document_list.append(line)
                if start==1:
                    # op += find1
                    with open('{0}pat1.txt'.format(str(cntr)), 'w') as opf:
                        opf.write(op)
                        opf.close()
                        op=''
                        cntr=cntr+1
                else:
                    start=1
            else:
                xml_document_list.append(line)
                op+= line


            print(op)
        f.close()




# fw= open(fname,'w')
# fw.write("hurray")
# line = fw.readline()
# print(line)
# fw.close()
