import challongegrabber

""" Basic test program """
def test():
    website = 'https://challonge.com/UoYUltimate39'
    bracket = challongegrabber.ChallongeGrabber(website)

    print(bracket.get_number_of_players())
    print(bracket.get_list_of_players())


if __name__ == "__main__":
    test()
