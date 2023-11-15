#! /usr/bin/env python3 
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler

import subprocess

# Exemplo de comando CMD no Windows
comando = 'ls'  # Substitua 'dir' pelo seu comando desejado

# Executar o comando
resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

# Exibir a saída do comando
print("Saída do comando:")
print(resultado.stdout)

# Exibir a saída de erro (se houver)
print("\nSaída de erro:")
print(resultado.stderr)



def inicio():
    #rclpy.init()
    nav = BasicNavigator()
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, 0.0)
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = nav.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = q_x
    initial_pose.pose.orientation.y = q_y
    initial_pose.pose.orientation.z = q_z
    initial_pose.pose.orientation.w = q_w

    nav.setInitialPose(initial_pose)
    nav.waitUntilNav2Active()
    #rclpy.shutdown()
    return True