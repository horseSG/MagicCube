
class GraphLetter:
    @classmethod
    def plot_letter_F(cls, ax, position=[0, 0, 0], extendDim=[1, 2], size=1.):
        x0, y0, z0 = position
        # Define the segments of the letter 'F'
        segments = [
            [(0, 0), (0, 5)],  # Vertical line
            [(0, 5), (3, 5)],  # Top horizontal line
            [(0, 2.5), (2, 2.5)]  # Middle horizontal line
        ]
        scale = 5

        cords = [[None] * 2 for _ in range(3)]
        fixDim = 3 - extendDim[0] - extendDim[1]
        cords[fixDim][0] = position[fixDim]
        cords[fixDim][1] = position[fixDim]
        for segment in segments:
            for i in range(2):      # two extend dimension
                tDim = extendDim[i]
                for j in range(2):  # start and end points
                    cords[tDim][j] = position[tDim] + size / scale * segment[j][i]
            ax.plot(cords[0], cords[1], cords[2], lw=2, color='k', zorder=2)

        
        # for segment in segments:
        #     x = [x0 + size * pt[0] for pt in segment]
        #     y = [y0 + size * pt[1] for pt in segment]
        #     z = [z0] * len(segment)
        #     ax.plot(x, y, z, color='black')