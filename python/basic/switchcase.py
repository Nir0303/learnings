def main():
    choices=dict (
                   one="first",
                   two="second"
                   )
    v="one"
    print(choices[v])
    v="three"
    print(choices.get(v,'other')) ## nvl condition

main()
