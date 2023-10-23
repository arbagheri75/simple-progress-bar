from time import sleep

# Print iterations progress
def print_progress_bar(iteration, total, length=50, prefix='', suffix='', decimal=1, filled='\u2588', blank='-', endbar='\r'):
    """
    \u2588
    Call in a loop to create a terminal progress bar
    @params:
        iteration   - Required : current iteration (int)
        total       - Required : total iteration (int)
        length      - Optional : character length of bar (int)
        prefix      - Optional : prefix string (str)
        suffix      - Optional : suffix string (str)
        decimal     - Optional : 

    """

    percent = ("{0:." + str(decimal) + "f}").format(100 * iteration / total)
    fill_space = length * iteration // total
    blank_space = length - fill_space
    bar = fill_space * filled + blank_space * blank

    print(f'{prefix} |{bar}|{suffix} {percent}%', end='\r')
    if iteration == total:
        print()


for num in range(27):
    print_progress_bar(num + 1, 27, 50, 'Progress', 'Complete')
    sleep(0.1)