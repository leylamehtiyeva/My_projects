
class TrackLine:
    """
    Defines a linear route segment
    """

    def __init__(self, to_x, to_y, max_speed):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_speed(self):
        return self._max_speed


class Track:
    """
    Creates a route track
    """

    def __init__(self, start_x, start_y):
        """
        Sets the initial position
        :param start_x: x coordinate
        :param start_y: y coordinate
        """
        self.start_x = start_x
        self.start_y = start_y
        self._tracks = []

    def add_track(self, tr):
        """
        Adds a segment to the track
        :param tr: track (from object TrackLine)
        """
        self._tracks.append(tr)

    def get_tracks(self):
        """
        :return: a tuple of track elements
        """
        return tuple(self._tracks)

    def __len__(self):
        """
        Calculates the Euclidean distance of the entire route
        :return: sum of all segments
        """
        len1 = ((self.start_x - self._tracks[0].x)**2 + (self.start_y - self._tracks[0].y)**2)**0.5
        return int(len1 + sum(self.__get_length(i) for i in range(1, len(self._tracks))))

    def __get_length(self, i):
        """
        Сalculates the euclidean distance of one segment (from i to i -1)
        :param i: current coordinate
        :return: the euclidean distance of segment [i, i-1]
        """
        return ((self._tracks[i-1].x - self._tracks[i].x)**2 + (self._tracks[i-1].y - self._tracks[i].y)**2)**0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)








