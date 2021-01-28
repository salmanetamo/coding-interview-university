def set_bit(x, position):
    mask = 1 << position
    return x | mask


def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask


def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask


def is_bit_set(x, position):
    shifted = x >> position
    return shifted & 1


def is_even(x):
    return (x & 1) == 0


def is_power_of_two(x):
    return (x & x - 1) == 0


print('Setting bit', str(bin(set_bit(0b00000110, 0b00000101))))
print('Clearing bit', str(bin(clear_bit(0b00000110, 0b00000010))))
print('Flipping bit', str(bin(flip_bit(0b00110110, 0b00000010))))
print('Is bit set', str(bin(is_bit_set(0b00110110, 3))))
print('Is even', str(is_even(0b00110110)))
print('Is power of two', str(is_power_of_two(0b00110110)))
