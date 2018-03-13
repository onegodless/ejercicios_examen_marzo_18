#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 12, 2018

@author: Jesús Molina
'''


from random import randrange


class Ejercicio5(object):
    '''
    classdocs
    '''
    __playerOneScore = 0
    __playerOneCard = 0
    __playerTwoScore = 0
    __playerTwoCard = 0
    

    def __init__(self):
        '''
        Constructor
        '''
    
    
    def gameLoop(self):
        '''
        Desc: Calls the methods of the class to run the game.
        
        Pre:
        
        Post:
        '''
        breakLoop = False
        thereIsWiner = False
        
        for x in range(3):
            self.cardGenerator()
            self.printCards()
            self.addScore()
            self.printRound()
            breakLoop = self.checkScore()
            if breakLoop == True:
                thereIsWiner = True
                break
            
        self.endOfRoundCheckScore(thereIsWiner)
        
        
    def cardGenerator(self):
        '''
        Desc: Generates two random numbers and assigns them to the class attributes.
        
        Pre:
        
        Post:
        '''
        self.__playerOneCard = randrange(1, 10)
        self.__playerTwoCard = randrange(1, 10)
    
    
    def printCards(self):
        '''
        Desc: Prints the numbers that were randomly generated in cardGenerator()
        
        Pre:
        
        Post:
        '''
        print "El jugador 1 saca: %d. El jugador 2 saca: %d." % (self.__playerOneCard, self.__playerTwoCard)        
        
        
    def addScore(self):
        '''
        Desc: adds the randomly generated numbers to the scores of both players.
        
        Pre:
        
        Post:
        '''
        self.__playerOneScore += self.__playerOneCard
        self.__playerTwoScore += self.__playerTwoCard    
        
        
    def printRound(self):
        '''
        Desc: Prints out the amount of score that both players have at the moment.
        
        Pre:
        
        Post:
        '''
        print 'El jugador uno tiene una suma de %d puntos.' % (self.__playerOneScore)
        print 'El jugador dos tiene una suma de %d puntos.' % (self.__playerTwoScore)


    def checkScore(self):
        '''
        Desc: Checks if the score of one of the players is higher than 15.
        
        Pre:
        
        Post: Calls the winerAnnoucement() method with the winer as an argument to print the winer of the match.
        '''
        if self.__playerOneScore > 15:
            self.winerAnnoucement('player2') 
        elif self.__playerTwoScore > 15:
            self.winerAnnoucement('player1')     
        
    
    def winerAnnoucement(self, winer):
        '''
        Desc: Prints the winer of the match.
        
        Pre: Takes a string that contains the winer of the match.
        
        Post:
        '''
        if winer == 'player1':
            print 'El jugador 1 gana.'
            return True
        
        elif winer == 'player2':
            print 'El jugador 2 gana.'
            return True
        
        elif winer == 'Draw':
            print 'Ha habido un empate.'
            return True
    
    def endOfRoundCheckScore(self, thereIsWiner):
        '''
        Desc: When the 3 rounds of the match are over this method checks the player with the higher score
        and pases that winer to the winerAnnoucement() method.
        
        Pre: Takes a boolean to check if one the players got more than 15 points before the match ended.
            If that is the case this method does nothing.
            
        Post: Calls winerAnnoucement() with an argument as string containing the winer of the match.
        '''
        if thereIsWiner == False:
            if self.__playerOneScore > self.__playerTwoScore:
                self.winerAnnoucement('player1')
            elif self.__playerOneScore < self.__playerTwoScore:
                self.winerAnnoucement('Player2')
            else:
                self.winerAnnoucement('Draw')
                                               
    