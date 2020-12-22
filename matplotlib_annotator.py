import matplotlib.pyplot as plt

class MatplotlibAnnotator:
    ##################
    # MatplotlibAnnotator is a tool that enables the interactive annotation of matplotlib charts
    # Needs to run with TK backend ( %matplotlib tk )

    def get_annotations(self):
        return self.annotations

    def __onclick(self, event):
        if (self.label_idx < len(self.labels)):
            cur_label = self.labels[self.label_idx]
            self.annotations[cur_label] = [event.xdata, event.ydata]
            self.label_idx += 1
        self.__redraw()

    def __redraw(self):
        self.ax.cla()
        self.ax.imshow(self.img)
        for label in self.annotations.keys():
            position = self.annotations[label]
            self.ax.text(position[0], position[1], label, bbox=dict(facecolor='#FFFFFF55', edgecolor='none'))
            self.ax.scatter(position[0], position[1], color="#FF0000")

        if (self.label_idx < len(self.labels)):
            cur_label = self.labels[self.label_idx]
            plt.title("Please click on {}".format(cur_label))
        else:
            plt.title("Annotation complete")

    def plot_annotate(self, img, labels):
        # INPUTS:
        # img: numpy array representing image
        # labels: name of labels to be annotated
        self.labels = labels
        self.label_idx = 0
        self.annotations = {}
        self.img = img
        (self.fig, (self.ax)) = plt.subplots(1, 1, figsize=(10,10)) 
        evt = self.__onclick
        self.callback_id = self.fig.canvas.mpl_connect('button_press_event', evt)
        self.__redraw()
        plt.show()