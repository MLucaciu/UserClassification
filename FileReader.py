class FileReader:
    '''
    Reads attributes from file
    '''
    @staticmethod
    def readAttributes(file_name):
        attributes = []
        with open(file_name) as f:
            for line in f:
                inner_list = [float(elt.strip()) for elt in line.split(',')]
                attributes.append(inner_list)
        return attributes

    '''
    Reads classes from file
    '''

    @staticmethod
    def readClasses(file_name):
        with open(file_name) as f:
            classes = f.readlines()
        classes = [x.strip() for x in classes]
        return classes
