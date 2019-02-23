import vrep # access all the VREP elements

class Jaco_arm_controller(object):
    def __init__(self):
        self.clientID = None
        self.joint_handles = []
        self.step = 10
        self.last_pos = []
    def set_up_connection(self):
        vrep.simxFinish(-1) # just in case, close all opened connections
        self.clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # start a connection

        if self.clientID!=-1:
            print ("Connected to remote API server")
            self.set_up_joints_handles()
        else:
            print("Not connected to remote API server")
            sys.exit("Could not connect")

        return


    def terminate_connection(self):
        vrep.simxStopSimulation(self.clientID,vrep.simx_opmode_oneshot)
        return

    def set_up_joints_handles(self):
        err_code1, joint_handle1 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint1",
                                        vrep.simx_opmode_blocking)
        err_code2, joint_handle2 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint2",
                                        vrep.simx_opmode_blocking)
        err_code3, joint_handle3 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint3",
                                        vrep.simx_opmode_blocking)
        err_code4, joint_handle4 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint4",
                                        vrep.simx_opmode_blocking)
        err_code5, joint_handle5 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint5",
                                        vrep.simx_opmode_blocking)
        err_code6, joint_handle6 = vrep.simxGetObjectHandle(
                                        self.clientID,
                                        "Jaco_joint6",
                                        vrep.simx_opmode_blocking)
        self.joint_handles = [joint_handle1,
                              joint_handle2,
                              joint_handle3,
                              joint_handle3,
                              joint_handle4,
                              joint_handle5,
                              joint_handle6]
        for i in range(6):
            self.last_pos.append(0)
        return

    def deg_to_rad(self, deg):
        rad = (deg*3.14)/180
        return rad

    def increase_joint_deg(self, joint_num):
        print(joint_num)
        err_code = vrep.simxSetJointTargetPosition(
                        self.clientID,
                        self.joint_handles[joint_num],
                        self.deg_to_rad(self.last_pos[joint_num]+self.step),
                        vrep.simx_opmode_streaming)
        self.last_pos[joint_num] +=self.step

        print(self.last_pos[joint_num]+self.step)

    def decrease_joint_deg(self, joint_num):
        err_code = vrep.simxSetJointTargetPosition(
                        self.clientID,
                        self.joint_handles[joint_num-1],
                        self.deg_to_rad(self.last_pos[joint_num-1]-self.step),
                        vrep.simx_opmode_streaming)
        self.last_pos[joint_num] -=self.step
        print(joint_num)
        print(self.last_pos[joint_num]+self.step)
