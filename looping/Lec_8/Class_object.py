def main():
    health = 100
    finish = False
    while not finish:
        print ('My health', health, 'heat me' )
        damage = int(input())
        health -= damage
        if health <= 0:
            finish = True
            print('You are win')


main()