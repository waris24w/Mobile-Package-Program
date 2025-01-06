packages = { 
    '1': 'Monthly Package',
    '2': 'Weekly Package',
    '3': 'Mini Package'
}

print('-------Packages-------')
for key, value in packages.items():
    print(f'{key:2}: {value}')
print('-----------------------')

price = 200
while True:
    pack = input("Select Package for Subscription (1, 2, or 3): ")
    selected_pack = packages.get(pack)
    
    if selected_pack:
        print(f"{selected_pack}: Price {price}")
        conf = input("Confirm the package to subscribe (y/n): ")
        
        if conf == 'n':
            print("\nPackage Cancelled :(")
            break
        elif conf == 'y':
            print('*********************************************')
            print('You have Successfully Subscribed to this bundle')
            print('*********************************************')
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    else:
        print("Invalid package selection. Please enter a valid option (1, 2, or 3).")
