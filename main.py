from math import sqrt


def readfile(file):
    data = list()
    with open(file, 'r') as files:
        for line in files:
            data.append(line.strip().split(','))
    return data


#calculate the distance between observations.
def euclidean_distance(oberv1, observ2):
    distance = 0.0
    #last column in each observation is a label
    for i in range(len(oberv1)-1):
        distance += (float(oberv1[i]) - float(observ2[i]))**2
    return sqrt(distance)

#nearest neighbour
def distance(train_set, test_set, k):
    distance = []
    for calculate in train_set:
        calculate_distance = euclidean_distance(test_set[:-1], calculate[:-1])
        distance.append((calculate, calculate_distance))
    distance.sort(key=lambda x: x[1])
    find_nearest = [x[0] for x in distance[:k]]
    return find_nearest

def lable_amount(k):
    lable_count = {}
    for neighbor in k:
        label = neighbor[-1]
        lable_count[label] = lable_count.get(label, 0) + 1
    predicted_label = max(lable_count, key=lable_count.get)
    return predicted_label

#accuracy for the entire set
def accuracy(actual_lable, predicted_lable):
    correct = 0.0
    for i in range(len(actual_lable)):
        if actual_lable[i] == predicted_lable[i]:
            correct += 1
    return (correct / float(len(actual_lable))) * 100.0

def main():
    training_path = input("Please, the path to the training file: ")
    training = readfile(training_path)

    # integer input
    k = int(input("Please, enter the number K: "))


    menu = {}
    menu['1'] = "Classification of all observations from the test set given in a separate file"
    menu['2'] = "Classification of the observation given by the user in the console"
    menu['3'] = "Change k"
    menu['4'] = "Exiting the program"

    while True:
        options = sorted(menu.keys())

        for enter in options:
            print(enter, menu[enter])
        choose = input("Please, choose an option: ")

        if choose == '1':
            test_path = input("Please, provide the path to the file with the test set: ")
            test = readfile(test_path)

            actual_lable = [x[-1] for x in test]
            predicted_lable = []

            for test_checker in test:
                print("Observations:", test_checker)
                nearest_neighbors = distance(training, test_checker, k)
                check_predicted_lable = lable_amount(nearest_neighbors)
                predicted_lable.append(check_predicted_lable)
                print("Predicted label:", check_predicted_lable)

            accuracy_value = accuracy(actual_lable, predicted_lable)
            print("Accuracy:", accuracy_value, "%")

        elif choose == '2':
            write_user = input("Please, enter N attributes separated by comma: ")
            observation = distance(training, write_user.split(", "), k)
            predict_lable = lable_amount(observation)
            print("Decision attribute:", predict_lable)

        elif choose == '3':
            k = int(input("Please, enter a new number K: "))

        elif choose == '4':
            break

        else:
            print("Unknown option was chosen!")

if __name__ == "__main__":
    main()