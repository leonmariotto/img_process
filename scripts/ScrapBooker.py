import numpy
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class ScrapBooker:
    """
    Class ScrapBooker
    """

    def __init__(self):
        """
        Init ScrapBooker
        """
        self.logger = logging.getLogger(__name__)

    def crop(self, array, dimensions, position=(0, 0)):
        """
        Crop an image with the following parameters :
            - dimension: a tuple with (x, y) position for end of crop
            (bottom-right)
            - position: a tuple with (x, y) position for start of crop
            (top-left)
        """
        new_array = array[position[1] : dimensions[1], position[0] : dimensions[0]]
        self.logger.debug(
            "Croping. Original array.shape=[%s]. dimension=[%s]"
            " position=[%s] new_array.shape=[%s]",
            str(array.shape),
            str(dimensions),
            str(position),
            str(new_array.shape),
        )
        return new_array

    def create_even_mask_1d(self, length, one_ratio=0.35):
        """
        Create a one-dimensional binary mask (an array of 0s and 1s) of the given length,
        where a specified fraction of the elements are 0 and the zeros are as evenly distributed as possible.

        Parameters:
            length (int): Length of the 1D mask.
            one_ratio (float): Fraction of ones desired (e.g., 0.35 for 35% ones).

        Returns:
            numpy.ndarray: A 1D numpy array containing only 0s and 1s.
        """
        if one_ratio > 1.0:
            raise ValueError()

        # Calculate the total number of zeros required by rounding to the nearest integer.
        total_zeros = int(round(length * (1.0 - one_ratio)))

        # Initialize the mask as an array filled with ones.
        mask = numpy.ones(length, dtype=int)

        # If no zeros are desired, return the all-ones mask immediately.
        if total_zeros <= 0:
            return mask

        # Use numpy.linspace to determine indices that are as evenly spaced as possible.
        # numpy.linspace returns evenly spaced values over the specified interval.
        # Setting dtype=int will floor the float values to integers.
        indices = numpy.linspace(0, length - 1, num=total_zeros, dtype=int)

        # Place zeros at the computed indices.
        mask[indices] = 0

        # Count the number of zeros actually placed (duplicates might occur when indices overlap).
        current_zeros = numpy.sum(mask == 0)

        self.logger.debug(
            "total_zeros=[%d] current_zeros=[%d] length=[%d]",
            total_zeros,
            current_zeros,
            length,
        )

        # If fewer zeros were placed than desired, add extra zeros at random positions where the mask is 1.
        if current_zeros < total_zeros:
            # Find the indices where the mask currently has ones.
            self.logger.debug("mask=[%s]", str(mask))
            available_indices = numpy.where(mask == 1)[0]
            self.logger.debug("available_indices=[%s]", str(available_indices))
            extra_needed = total_zeros - current_zeros
            # Randomly choose the required number of extra positions (without replacement).
            extra_indices = numpy.random.choice(
                available_indices, size=extra_needed, replace=False
            )
            mask[extra_indices] = 0

        # If more zeros were placed (unlikely in this approach), remove some zeros randomly.
        elif current_zeros > total_zeros:
            zero_indices = numpy.where(mask == 0)[0]
            extra = current_zeros - total_zeros
            # Randomly choose indices to change back to one.
            remove_indices = numpy.random.choice(
                zero_indices, size=extra, replace=False
            )
            mask[remove_indices] = 1

        return mask

    def thin(self, array, dimensions):
        """
        Reduce an image with the following parameters :
            - dimension: a tuple with (x, y) position of end of image
            (bottom-right)
        """
        one_ratio_x = dimensions[0] / array.shape[1]
        one_ratio_y = dimensions[1] / array.shape[0]
        self.logger.error(
            "Original array.shape=[%s]. dimension=[%s] one_ratio_x=%f, one_ratio_y=%f",
            str(array.shape),
            str(dimensions),
            one_ratio_x,
            one_ratio_y,
        )
        x_mask = self.create_even_mask_1d(array.shape[1], one_ratio_x)
        y_mask = self.create_even_mask_1d(array.shape[0], one_ratio_y)
        array_thin_x = numpy.delete(array, numpy.where(x_mask == 0), 1)
        new_array = numpy.delete(array_thin_x, numpy.where(y_mask == 0), 0)
        self.logger.debug("Thined. new_array.shape=[%s]", str(new_array.shape))
        return new_array

    def oldthin(self, array, n, axis):
        if axis == 0 or axis == 1:
            array = numpy.delete(array, slice(None, None, n), axis)
        else:
            raise ValueError("Axis must be 0 or 1")
        return array

    def thinundershape(self, array, x, y, shape):
        if shape[0] < array.shape[0]:
            array = numpy.delete(array, slice(None, None, y), 0)
        if shape[1] < array.shape[1]:
            array = numpy.delete(array, slice(None, None, x), 1)
        return array

    def thinall(self, array, x, y):
        array = numpy.delete(array, slice(None, None, y), 0)
        array = numpy.delete(array, slice(None, None, x), 1)
        return array

    def juxtapose(self, array, n, axis):
        if axis < 0 or axis > 1:
            raise ValueError("Axis must be 0 or 1")
        array = numpy.concatenate([array for i in range(n)], axis)
        return array

    def mosaic(self, array, dimensions):
        array = numpy.concatenate([array for i in range(dimensions[0])], 0)
        array = numpy.concatenate([array for i in range(dimensions[1])], 1)
        return array

    def border(self, array, size: int, mode: str):
        self.logger.debug("Added border of size %d with mode %s", size, mode)
        shape = array.shape
        if mode == "erase":
            array[::, 0:size, ::] = 0
            array[0:size, ::, ::] = 0
            array[::, shape[1] - size : shape[1], ::] = 0
            array[shape[0] - size : shape[0], ::, ::] = 0
            newarray = array
        else:
            raise ValueError("Only replace mode supported")
        return newarray

    # def concate(self, array, x, y, axis):
    #      for i in range(1, y, x)
    #  		line = numpy.concatenate([array for i in range(x)], 0)
    #
    #  res = numpy.concatenate([array for i in range(x)], 0)
    #  res = numpy.concatenate([array for i in range(y)], 1)
    #  return array

    # def concate_line(self, array, x, axis):
    #  res = numpy.concatenate(array, 0)
    #  return res
