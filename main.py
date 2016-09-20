from pl_monitor import pl_site_up
from mt_monitor import mt_site_up
from tlp_monitor import tlp_site_up



def tlp_print():
    print()
    print('-'*50)
    print()
    print("Checking Tight Line Production Clients")
    print()
    print('-'*50)
    print()

def pl_print():
    print()
    print('-'*50)
    print()
    print("Checking Plutonium Production Clients")
    print()
    print('-'*50)
    print()

def mt_print():
    print()
    print('-'*50)
    print()
    print("Checking Media Temple TLP Clients")
    print()
    print('-'*50)
    print()


def main():
    pl_print()
    pl_site_up()
    mt_print()
    mt_site_up()
    tlp_print()
    tlp_site_up()

main()
