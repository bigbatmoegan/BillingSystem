class fileIO:
    def __init__(self, array, filename):
        self.array=array
        self.filename=filename

    def writer(self):
        with open (self.filename,'w', newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(self.array)

    

