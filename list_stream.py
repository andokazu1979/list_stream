class ListStream(object):
    """Generator for stream of lists"""

    @staticmethod
    def get_comb(lists_in, lst_out=None, n=0):
        """Get generator for combination of the input lists

        :param lists_in: list of ingredient
        :param lst_out: generated list
        :param n: used for recursive call
        """
        if lst_out is None:
            lst_out = []
        for item in lists_in[n]:
            lst_out.append(item)
            if n != len(lists_in) - 1:
                for g in ListStream.get_comb(lists_in, lst_out, n + 1):
                    yield g
                lst_out.pop()
            else:
                yield lst_out
                lst_out.pop()

    @staticmethod
    def get_1to1(lists_in):
        """Get generator for 1 to 1 correspondence of the input lists"""

        for i, _ in enumerate(lists_in[0]):
            lst_out = []
            for lst_in in lists_in:
                lst_out.append(lst_in[i])
            yield lst_out

