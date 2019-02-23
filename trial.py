import tkinter as tk
from  bubbleRob_control import Jaco_arm_controller

def set_arrows_up(arrow_up ,main_window, controller):
    j_arrows_up = []
    j1_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(0))
    j2_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(1))
    j3_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(2))
    j4_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(3))
    j5_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(4))
    j6_arrow_up = tk.Button(main_window,
                        image=arrow_up,
                        command=lambda : controller.increase_joint_deg(5))
    j_arrows_up.append(j1_arrow_up)
    j_arrows_up.append(j2_arrow_up)
    j_arrows_up.append(j3_arrow_up)
    j_arrows_up.append(j4_arrow_up)
    j_arrows_up.append(j5_arrow_up)
    j_arrows_up.append(j6_arrow_up)
    return j_arrows_up

def set_arrows_down(arrow_down, main_window, controller):
    j_arrows_down = []
    j1_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(0))
    j2_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(1))
    j3_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(2))
    j4_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(3))
    j5_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(4))
    j6_arrow_down = tk.Button(main_window,
                        image=arrow_down,
                        command=lambda : controller.decrease_joint_deg(5))
    j_arrows_down.append(j1_arrow_down)
    j_arrows_down.append(j2_arrow_down)
    j_arrows_down.append(j3_arrow_down)
    j_arrows_down.append(j4_arrow_down)
    j_arrows_down.append(j5_arrow_down)
    j_arrows_down.append(j6_arrow_down)
    return j_arrows_down


def main():
    controller = Jaco_arm_controller()
    main_window = tk.Tk()

    main_window.title('joint control')
    main_window.geometry('400x400')

    #HEADER TEXT
    header1 = tk.Label(main_window,
                        text="Jaco arm control",
                        padx = 20,
                        pady = 10,
                        font ="Helvetica 16 bold")
    header1.grid(row = 0, column = 0)


    arrow_up = tk.PhotoImage(file="arrow_up.png").subsample(30, 30)
    arrow_down = tk.PhotoImage(file="arrow_down.png").subsample(30, 30)

    j_header_labels = []
    j_arrows_up = set_arrows_up(arrow_up, main_window, controller)
    j_arrows_down = set_arrows_down(arrow_down, main_window, controller)

    for i in range(6):
        j = tk.Label(main_window,
                            text="J"+str(i+1),
                            padx = 10,
                            pady = 10,
                            font ="Helvetica 12 bold")
        j.grid(row = i+1, column = 0)
        j_header_labels.append(j)

        j_arrows_up[i].grid(row = i+1, column = 1)
        j_arrows_down[i].grid(row = i+1, column = 2)


    #connect button
    connect_bttn = tk.Button(main_window,
                            text="Connect",
                            command=controller.set_up_connection)
    connect_bttn.grid(row = 7, column = 0)

    #disconnect button
    disconnect_bttn = tk.Button(main_window,
                            text="Disconnect",
                            command=controller.terminate_connection)
    disconnect_bttn.grid(row = 7, column = 2)

    main_window.mainloop()



    return
if __name__ == '__main__':
    main()
