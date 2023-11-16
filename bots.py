import threading
import json
import time

with open('inventory.dat', 'r') as file:
    inventory = json.load(file)

def bot_clerk(items_list):
    cart_list = []
    thread_lock = threading.Lock()

    robot_fetcher_lists = []

    for i in range(3):
        robot_fetcher_lists.append([])
        
    for i, item in enumerate(items_list):
        robot_fetcher_lists[i % 3].append([item, *inventory[item]])

    threads = [threading.Thread(target=bot_fetcher, args=(fetcher_list, cart_list, thread_lock)) for fetcher_list in robot_fetcher_lists]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return cart_list

def bot_fetcher(item_list, cart_list, thread_lock):
    for item_num in item_list:
        time.sleep(item_num[2])
        
        with thread_lock:
            item = [item_num[0], item_num[1]]
            cart_list.append(item)

