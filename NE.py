'''
This code is a really simple implementation of finding Nash Equilibrium for a game like this:
There are two players,
each player has two moods,
the probablity of player 1 being in first mood is beta,
the probablity of player 1 being in second mood is 1 - beta,
the probablity of player 2 being in first mood is alpha,
the probablity of player 1 being in second mood is 1 - alpha.
As you can expect, there should be 4 score tables.
In these score tables we should see how much each player gains for each action.
For example these are score tables for a sample game:
    table 1        table 2
[2, 1], [0, 0]  [2, 0], [0, 2]
[0, 0], [1, 2]  [0, 1], [1, 0]
    table 3        table 4
[0, 1], [2, 0]  [0, 0], [2, 2]
[1, 0], [0, 2]  [1, 1], [0, 0]

to give the above tables as input to the program, ypu should give each of the following line as input for each table.
[2, 1], [0, 0], [0, 0], [1, 2]
[2, 0], [0, 2], [0, 1], [1, 0]
[0, 1], [2, 0], [1, 0], [0, 2]
[0, 0], [2, 2], [1, 1], [0, 0]
'''

import tkinter as tk
from tkinter import ttk
import numpy as np
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#example input
#payoff_matrix_1_medium_2_strong = np.array([[-1, 1], [1, 0], [0, 1], [0, 0]])
#payoff_matrix_1_medium_2_weak = np.array([[1, -1], [1, 0], [0, 1], [0, 0]])
#payoff_matrix_1_strong_2_strong = np.array([[1, -1], [1, 0], [0, 1], [0, 1]])
#payoff_matrix_1_strong_2_weak = np.array([[1, -1], [1, 0], [0, -1], [0, 0]])

#example input 2 for bakh stra....
#payoff_matrix_1_medium_2_strong = np.array([[2, 1], [0, 0], [0, 0], [1, 2]])
#payoff_matrix_1_medium_2_weak = np.array([[2, 0], [0, 2], [0, 1], [1, 0]])
#payoff_matrix_1_strong_2_strong = np.array([[0, 1], [2, 0], [1, 0], [0, 2]])
#payoff_matrix_1_strong_2_weak = np.array([[0, 0], [2, 2], [1, 1], [0, 0]])

#payoff_matrix_1_medium_2_strong = np.array([[20, 11], [0, 0], [0,0], [0, 0]])


class GameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nash Equilibrium Calculator")
        self.root.geometry('600x600')

        self.payoff_matrices = [
            "payoff_matrix_1_medium_2_strong",
            "payoff_matrix_1_medium_2_weak",
            "payoff_matrix_1_strong_2_strong",
            "payoff_matrix_1_strong_2_weak"
        ]

        self.entry_vars = {}
        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for payoff matrices
        for i, matrix_name in enumerate(self.payoff_matrices):
            matrix_label = tk.Label(self.root, text=f"Enter {matrix_name} as a list:")
            matrix_label.grid(row=i, column=2, pady=20)

            entry_var = tk.StringVar()
            matrix_entry = tk.Entry(self.root, textvariable=entry_var)
            matrix_entry.grid(row=i, column=3, pady=20)

            self.entry_vars[matrix_name] = entry_var

        # Create labels and entry fields for alpha and beta
        alpha_label = tk.Label(self.root, text="Enter alpha:")
        alpha_label.grid(row=len(self.payoff_matrices), column=2, pady=20)

        self.alpha_entry = tk.Entry(self.root)
        self.alpha_entry.grid(row=len(self.payoff_matrices), column=3, pady=20)

        beta_label = tk.Label(self.root, text="Enter beta:")
        beta_label.grid(row=len(self.payoff_matrices) + 1, column=2, pady=20)

        self.beta_entry = tk.Entry(self.root)
        self.beta_entry.grid(row=len(self.payoff_matrices) + 1, column=3, pady=20)

        # Create a button to calculate Nash Equilibrium
        calculate_button = tk.Button(self.root, text="Calculate Nash Equilibrium", command=self.calculate_nash_equilibrium)
        calculate_button.grid(row=len(self.payoff_matrices) + 2, column=3, columnspan=2, pady=20)

    def calculate_nash_equilibrium(self):
        # Get user input for payoff matrices
        payoff_matrices = [np.array(eval(self.entry_vars[matrix_name].get())) for matrix_name in self.payoff_matrices]

        # Get user input for alpha and beta
        alpha_value = float(self.alpha_entry.get())
        beta_value = float(self.beta_entry.get())

        self.calculate_nash_equilibrium_function(alpha_value, beta_value, payoff_matrices)

    def calculate_nash_equilibrium_function(self, alpha, beta, payoff_matrices):
        payoff_matrix_1_medium_2_strong, payoff_matrix_1_medium_2_weak, payoff_matrix_1_strong_2_strong, payoff_matrix_1_strong_2_weak = payoff_matrices
        
        # Player 1 probabilities
        p_medium = round(beta, 2)
        p_strong = round(1 - beta, 2)
        # Player 2 probabilities
        q_strong = round(alpha, 2)
        q_weak = round(1 - alpha, 2)
        
        
        
        ######## now We should create 4 new tables that show each player's expected payoffs on each mood.######
        matrix_player_1_in_medium_day = [
                [
                 payoff_matrix_1_medium_2_strong[0,0] * q_strong + payoff_matrix_1_medium_2_weak[0,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[0,0] * q_strong + payoff_matrix_1_medium_2_weak[1,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[1,0] * q_strong + payoff_matrix_1_medium_2_weak[0,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[1,0] * q_strong + payoff_matrix_1_medium_2_weak[1,0] * q_weak
                ],
                [
                 payoff_matrix_1_medium_2_strong[2,0] * q_strong + payoff_matrix_1_medium_2_weak[2,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[2,0] * q_strong + payoff_matrix_1_medium_2_weak[3,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[3,0] * q_strong + payoff_matrix_1_medium_2_weak[2,0] * q_weak,
                 payoff_matrix_1_medium_2_strong[3,0] * q_strong + payoff_matrix_1_medium_2_weak[3,0] * q_weak
                ]
                ]
        
        matrix_player_1_in_strong_day = [
                [
                 payoff_matrix_1_strong_2_strong[0,0] * q_strong + payoff_matrix_1_strong_2_weak[0,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[0,0] * q_strong + payoff_matrix_1_strong_2_weak[1,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[1,0] * q_strong + payoff_matrix_1_strong_2_weak[0,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[1,0] * q_strong + payoff_matrix_1_strong_2_weak[1,0] * q_weak
                ],
                [
                 payoff_matrix_1_strong_2_strong[2,0] * q_strong + payoff_matrix_1_strong_2_weak[2,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[2,0] * q_strong + payoff_matrix_1_strong_2_weak[3,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[3,0] * q_strong + payoff_matrix_1_strong_2_weak[2,0] * q_weak,
                 payoff_matrix_1_strong_2_strong[3,0] * q_strong + payoff_matrix_1_strong_2_weak[3,0] * q_weak
                ]
                ]
        
        matrix_player_2_in_strong_day = [
                [
                 payoff_matrix_1_medium_2_strong[0,1] * p_medium + payoff_matrix_1_strong_2_strong[0,1] * p_strong,
                 payoff_matrix_1_medium_2_strong[1,1] * p_medium + payoff_matrix_1_strong_2_strong[1,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_strong[0,1] * p_medium + payoff_matrix_1_strong_2_strong[2,1] * p_strong,
                 payoff_matrix_1_medium_2_strong[1,1] * p_medium + payoff_matrix_1_strong_2_strong[3,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_strong[2,1] * p_medium + payoff_matrix_1_strong_2_strong[0,1] * p_strong,
                 payoff_matrix_1_medium_2_strong[3,1] * p_medium + payoff_matrix_1_strong_2_strong[1,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_strong[2,1] * p_medium + payoff_matrix_1_strong_2_strong[2,1] * p_strong,
                 payoff_matrix_1_medium_2_strong[3,1] * p_medium + payoff_matrix_1_strong_2_strong[3,1] * p_strong
                ]
                ]
        
        matrix_player_2_in_weak_day = [
                [
                 payoff_matrix_1_medium_2_weak[0,1] * p_medium + payoff_matrix_1_strong_2_weak[0,1] * p_strong,
                 payoff_matrix_1_medium_2_weak[1,1] * p_medium + payoff_matrix_1_strong_2_weak[1,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_weak[0,1] * p_medium + payoff_matrix_1_strong_2_weak[2,1] * p_strong,
                 payoff_matrix_1_medium_2_weak[1,1] * p_medium + payoff_matrix_1_strong_2_weak[3,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_weak[2,1] * p_medium + payoff_matrix_1_strong_2_weak[0,1] * p_strong,
                 payoff_matrix_1_medium_2_weak[3,1] * p_medium + payoff_matrix_1_strong_2_weak[1,1] * p_strong,
                ],
                [
                 payoff_matrix_1_medium_2_weak[2,1] * p_medium + payoff_matrix_1_strong_2_weak[2,1] * p_strong,
                 payoff_matrix_1_medium_2_weak[3,1] * p_medium + payoff_matrix_1_strong_2_weak[3,1] * p_strong
                ]
                ]
        matrix_player_1_in_medium_day = np.array(matrix_player_1_in_medium_day)
        matrix_player_1_in_strong_day = np.array(matrix_player_1_in_strong_day)
        matrix_player_2_in_strong_day = np.array(matrix_player_2_in_strong_day)
        matrix_player_2_in_weak_day = np.array(matrix_player_2_in_weak_day)
        #####################################################################################
        #####################################################################################
        #lets check the data for all payoffs.
        print("/////////////Here is The Score Tables/////////////")
        print (payoff_matrix_1_medium_2_strong[0],payoff_matrix_1_medium_2_strong[1],"\t",payoff_matrix_1_medium_2_weak[0],payoff_matrix_1_medium_2_weak[1])
        print (payoff_matrix_1_medium_2_strong[2],payoff_matrix_1_medium_2_strong[3],"\t",payoff_matrix_1_medium_2_weak[2],payoff_matrix_1_medium_2_weak[3],"\n")
        print (payoff_matrix_1_strong_2_strong[0],payoff_matrix_1_strong_2_strong[1],"\t",payoff_matrix_1_strong_2_weak[0],payoff_matrix_1_strong_2_weak[1])
        print (payoff_matrix_1_strong_2_strong[2],payoff_matrix_1_strong_2_strong[3],"\t",payoff_matrix_1_strong_2_weak[2],payoff_matrix_1_strong_2_weak[3],"\n")
        print("//////////////////////////////////////////////////")
        print("////////Here is The Expected Payoff Tables////////")
        print (matrix_player_1_in_medium_day,"\n")
        print (matrix_player_1_in_strong_day,"\n")
        print (matrix_player_2_in_strong_day,"\n")
        print (matrix_player_2_in_weak_day,"\n")
        print("///////////////////////////////////////////////////")
        #####################################################################################
        ###################Now we should find best response for each player.#################
        p1_BB_br_p2 = ""
        p1_BS_br_p2 = ""
        p1_SB_br_p2 = ""
        p1_SS_br_p2 = ""
        
        p2_BB_br_p1 = ""
        p2_BS_br_p1 = ""
        p2_SB_br_p1 = ""
        p2_SS_br_p1 = ""
        
        if matrix_player_1_in_medium_day[0,0] > matrix_player_1_in_medium_day[1,0]:
            p2_BB_br_p1 += "B"
        elif matrix_player_1_in_medium_day[0,0] == matrix_player_1_in_medium_day[1,0]:
            p2_BB_br_p1 += "D" #means dont care
        else:
            p2_BB_br_p1 += "S"
            
        if matrix_player_1_in_medium_day[0,1] > matrix_player_1_in_medium_day[1,1]:
            p2_BS_br_p1 += "B"
        elif matrix_player_1_in_medium_day[0,1] == matrix_player_1_in_medium_day[1,1]:
            p2_BS_br_p1 += "D" #means dont care
        else:
            p2_BS_br_p1 += "S"
            
        if matrix_player_1_in_medium_day[0,2] > matrix_player_1_in_medium_day[1,2]:
            p2_SB_br_p1 += "B"
        elif matrix_player_1_in_medium_day[0,2] == matrix_player_1_in_medium_day[1,2]:
            p2_SB_br_p1 += "D" #means dont care
        else:
            p2_SB_br_p1 += "S"
            
        if matrix_player_1_in_medium_day[0,3] > matrix_player_1_in_medium_day[1,3]:
            p2_SS_br_p1 += "B"
        elif matrix_player_1_in_medium_day[0,3] == matrix_player_1_in_medium_day[1,3]:
            p2_SS_br_p1 += "D" #means dont care
        else:
            p2_SS_br_p1 += "S"
        ####################
        if matrix_player_1_in_strong_day[0,0] > matrix_player_1_in_strong_day[1,0]:
            p2_BB_br_p1 += "B"
        elif matrix_player_1_in_strong_day[0,0] == matrix_player_1_in_strong_day[1,0]:
            p2_BB_br_p1 += "D" #means dont care
        else:
            p2_BB_br_p1 += "S"
            
        if matrix_player_1_in_strong_day[0,1] > matrix_player_1_in_strong_day[1,1]:
            p2_BS_br_p1 += "B"
        elif matrix_player_1_in_strong_day[0,1] == matrix_player_1_in_strong_day[1,1]:
            p2_BS_br_p1 += "D" #means dont care
        else:
            p2_BS_br_p1 += "S"
            
        if matrix_player_1_in_strong_day[0,2] > matrix_player_1_in_strong_day[1,2]:
            p2_SB_br_p1 += "B"
        elif matrix_player_1_in_strong_day[0,2] == matrix_player_1_in_strong_day[1,2]:
            p2_SB_br_p1 += "D" #means dont care
        else:
            p2_SB_br_p1 += "S"
            
        if matrix_player_1_in_strong_day[0,3] > matrix_player_1_in_strong_day[1,3]:
            p2_SS_br_p1 += "B"
        elif matrix_player_1_in_strong_day[0,3] == matrix_player_1_in_strong_day[1,3]:
            p2_SS_br_p1 += "D" #means dont care
        else:
            p2_SS_br_p1 += "S"   
        ####################
        if matrix_player_2_in_strong_day[0,0] > matrix_player_2_in_strong_day[0,1]:
            p1_BB_br_p2 += "B"
        elif matrix_player_2_in_strong_day[0,0] == matrix_player_2_in_strong_day[0,1]:
            p1_BB_br_p2 += "D" #means dont care
        else:
            p1_BB_br_p2 += "S"
            
        if matrix_player_2_in_strong_day[1,0] > matrix_player_2_in_strong_day[1,1]:
            p1_BS_br_p2 += "B"
        elif matrix_player_2_in_strong_day[1,0] == matrix_player_2_in_strong_day[1,1]:
            p1_BS_br_p2 += "D" #means dont care
        else:
            p1_BS_br_p2 += "S"
            
        if matrix_player_2_in_strong_day[2,0] > matrix_player_2_in_strong_day[2,1]:
            p1_SB_br_p2 += "B"
        elif matrix_player_2_in_strong_day[2,0] == matrix_player_2_in_strong_day[2,1]:
            p1_SB_br_p2 += "D" #means dont care
        else:
            p1_SB_br_p2 += "S"
            
        if matrix_player_2_in_strong_day[3,0] > matrix_player_2_in_strong_day[3,1]:
            p1_SS_br_p2 += "B"
        elif matrix_player_2_in_strong_day[3,0] == matrix_player_2_in_strong_day[3,1]:
            p1_SS_br_p2 += "D" #means dont care
        else:
            p1_SS_br_p2 += "S"
        ####################
        if matrix_player_2_in_weak_day[0,0] > matrix_player_2_in_weak_day[0,1]:
            p1_BB_br_p2 += "B"
        elif matrix_player_2_in_weak_day[0,0] == matrix_player_2_in_weak_day[0,1]:
            p1_BB_br_p2 += "D" #means dont care
        else:
            p1_BB_br_p2 += "S"
            
        if matrix_player_2_in_weak_day[1,0] > matrix_player_2_in_weak_day[1,1]:
            p1_BS_br_p2 += "B"
        elif matrix_player_2_in_weak_day[1,0] == matrix_player_2_in_weak_day[1,1]:
            p1_BS_br_p2 += "D" #means dont care
        else:
            p1_BS_br_p2 += "S"
            
        if matrix_player_2_in_weak_day[2,0] > matrix_player_2_in_weak_day[2,1]:
            p1_SB_br_p2 += "B"
        elif matrix_player_2_in_weak_day[2,0] == matrix_player_2_in_weak_day[2,1]:
            p1_SB_br_p2 += "D" #means dont care
        else:
            p1_SB_br_p2 += "S"
            
        if matrix_player_2_in_weak_day[3,0] > matrix_player_2_in_weak_day[3,1]:
            p1_SS_br_p2 += "B"
        elif matrix_player_2_in_weak_day[3,0] == matrix_player_2_in_weak_day[3,1]:
            p1_SS_br_p2 += "D" #means dont care
        else:
            p1_SS_br_p2 += "S"        
        ####################
        print ("//Here are the BR's for Each Player//")
        print ("Player 1 Best Response for BB is: ", p2_BB_br_p1)
        print ("Player 1 Best Response for BB is: ", p2_BS_br_p1)
        print ("Player 1 Best Response for BB is: ", p2_SB_br_p1)
        print ("Player 1 Best Response for BB is: ", p2_SS_br_p1)
        print ("////////////////////////////////////")
        print ("Player 2 Best Response for BB is: ", p1_BB_br_p2)
        print ("Player 2 Best Response for BS is: ", p1_BS_br_p2)
        print ("Player 2 Best Response for SB is: ", p1_SB_br_p2)
        print ("Player 2 Best Response for SS is: ", p1_SS_br_p2)
        print ("////////////////////////////////////////////////////")
        
        print ("\n","Nash Equilibrium:","\n")
        counter = 0
        match p1_BB_br_p2:
            case "BB":
                if p2_BB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BB,BB)")
                    counter+=1
            case "BS":
                if p2_BS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BS,BB)")
                    counter+=1
            case "SB":
                if p2_SB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SB,BB)")
                    counter+=1
            case "SS":
                if p2_SS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SS,BB)")
                    counter+=1
            case "DS":
                if p2_BS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BS,BB)")
                    counter+=1
                if p2_SS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SS,BB)")
                    counter+=1
            case "DB":
                if p2_BB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BB,BB)")
                    counter+=1
                if p2_SB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SB,BB)")
                    counter+=1
            case "SD":
                if p2_SS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SS,BB)")
                    counter+=1
                if p2_SB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SB,BB)")    
                    counter+=1
            case "BD":
                if p2_BS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BS,BB)")
                    counter+=1
                if p2_BB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BB,BB)")
                    counter+=1
            case "DD":
                if p2_BB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BB,BB)")
                    counter+=1
                if p2_BS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(BS,BB)")
                    counter+=1
                if p2_SB_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SB,BB)")
                    counter+=1
                if p2_SS_br_p1 in ("BB", "BD", "DB", "DD"):
                    print ("(SS,BB)")
                    counter+=1
                    
        match p1_BS_br_p2:
            case "BB":
                if p2_BB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BB,BS)")
                    counter+=1
            case "BS":
                if p2_BS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BS,BS)")
                    counter+=1
            case "SB":
                if p2_SB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SB,BS)")
                    counter+=1
            case "SS":
                if p2_SS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SS,BS)")
                    counter+=1
            case "DS":
                if p2_BS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BS,BS)")
                    counter+=1
                if p2_SS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SS,BS)")
                    counter+=1
            case "DB":
                if p2_BB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BB,BS)")
                    counter+=1
                if p2_SB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SB,BS)")
                    counter+=1
            case "SD":
                if p2_SS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SS,BS)")
                    counter+=1
                if p2_SB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SB,BS)")    
                    counter+=1
            case "BD":
                if p2_BS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BS,BS)")
                    counter+=1
                if p2_BB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BB,BS)")
                    counter+=1
            case "DD":
                if p2_BB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BB,BS)")
                    counter+=1
                if p2_BS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(BS,BS)")
                    counter+=1
                if p2_SB_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SB,BS)")
                    counter+=1
                if p2_SS_br_p1 in ("BS", "BD", "DS", "DD"):
                    print ("(SS,BS)")
                    counter+=1
        
        match p1_SB_br_p2:
            case "BB":
                if p2_BB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BB,SB)")
                    counter+=1
            case "BS":
                if p2_BS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BS,SB)")
                    counter+=1
            case "SB":
                if p2_SB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SB,SB)")
                    counter+=1
            case "SS":
                if p2_SS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SS,SB)")
                    counter+=1
            case "DS":
                if p2_BS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BS,SB)")
                    counter+=1
                if p2_SS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SS,SB)")
                    counter+=1
            case "DB":
                if p2_BB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BB,SB)")
                    counter+=1
                if p2_SB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SB,SB)")
                    counter+=1
            case "SD":
                if p2_SS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SS,SB)")
                    counter+=1
                if p2_SB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SB,SB)")    
                    counter+=1
            case "BD":
                if p2_BS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BS,SB)")
                    counter+=1
                if p2_BB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BB,SB)")
                    counter+=1
            case "DD":
                if p2_BB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BB,SB)")
                    counter+=1
                if p2_BS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(BS,SB)")
                    counter+=1
                if p2_SB_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SB,SB)")
                    counter+=1
                if p2_SS_br_p1 in ("SB", "SD", "DB", "DD"):
                    print ("(SS,SB)")
                    counter+=1
        
        match p1_SS_br_p2:
            case "BB":
                if p2_BB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BB,SS)")
                    counter+=1
            case "BS":
                if p2_BS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BS,SS)")
                    counter+=1
            case "SB":
                if p2_SB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SB,SS)")
                    counter+=1
            case "SS":
                if p2_SS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SS,SS)")
                    counter+=1
            case "DS":
                if p2_BS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BS,SS)")
                    counter+=1
                if p2_SS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SS,SS)")
                    counter+=1
            case "DB":
                if p2_BB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BB,SS)")
                    counter+=1
                if p2_SB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SB,SS)")
                    counter+=1
            case "SD":
                if p2_SS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SS,SS)")
                    counter+=1
                if p2_SB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SB,SS)")    
                    counter+=1
            case "BD":
                if p2_BS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BS,SS)")
                    counter+=1
                if p2_BB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BB,SS)")
                    counter+=1
            case "DD":
                if p2_BB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BB,SS)")
                    counter+=1
                if p2_BS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(BS,SS)")
                    counter+=1
                if p2_SB_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SB,SS)")
                    counter+=1
                if p2_SS_br_p1 in ("SS", "SD", "DS", "DD"):
                    print ("(SS,SS)")
                    counter+=1
            
        print ("There Are", counter, "Pure Nash Equilibriums For this Game.")
        print("////////////////////////////////////////////////////////")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()