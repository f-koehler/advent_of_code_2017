import numpy

if __name__ == "__main__":
    with open("input_01.txt") as fhandle:
        captcha = numpy.array([int(char) for char in fhandle.read().strip()])
    print(sum(captcha[captcha == numpy.roll(captcha, 1)]))
    print(sum(captcha[captcha == numpy.roll(captcha, len(captcha) // 2)]))
