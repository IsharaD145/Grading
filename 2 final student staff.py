from graphics import *

# Global variables
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludedCount = 0



def main():
    choice = 'y'
    while choice == 'y':
        try:
            global progressCount, trailerCount, retrieverCount, excludedCount, displayer, passCredit, deferCredit, failCredit
            # Getting user input
            inputValue = 'Enter your total PASS credits: '
            passCredit = rangeChecker(inputValue)

            inputValue = 'Enter your total DEFER credits: '
            deferCredit = rangeChecker(inputValue)

            inputValue = 'Enter your total FAIL credits: '
            failCredit = rangeChecker(inputValue)

            totalCredit = passCredit + deferCredit + failCredit

            # checking for the total to be greater than 120 and check the inputs for the proper inputs
            if totalCredit != 120:
                print('Total incorrect')
                continue

            # checking for the credit volumes for pass
            if passCredit == 120:
                displayer = "Progress"
                print(displayer,' \n')
                progressCount += 1


            # checking for the credit volumes for pass(module trailer)
            elif passCredit == 100:
                displayer = "Progress(module trailer)"
                print(displayer,'\n')
                trailerCount += 1


            elif (passCredit in (20, 0, 40)) and (deferCredit in (0, 20, 40)) and (failCredit in (80, 100, 120)):
                displayer ="Excluded"
                print( displayer,'\n')
                excludedCount += 1

            else:
                displayer = "module retriever"
                print(displayer, '\n')
                retrieverCount += 1

            if position == 'student':
                exit()

            records.append(f"{displayer} - {passCredit}, {deferCredit}, {failCredit}")

            # getting users choice to run the iteration
            while True:
                choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
                if choice not in ['q', 'y']:
                    print("Invalid choice")
                else:
                    break
        except ValueError:
            print('Integer Required')


def rangeChecker(inputValue):
    while True:
        try:
            value = float(input(inputValue))

            if value in (0, 20, 40, 60, 80, 100, 120):
                value = int(value)
                return value
            else:
                print('Out of range')
        except ValueError:
            print('Integer Required')


def histogram(progress, trailer, retriever, excluded):
    """Histogram for the count of grades"""
    try:

        win = GraphWin("Histogram", 800, 600)
        win.setBackground("Mint Cream")

        # Histogram text at the top
        topTxt = Text(Point(200, 30), "Histogram Results")
        topTxt.draw(win)
        topTxt.setSize(28)
        topTxt.setStyle("bold")
        topTxt.setTextColor("grey")

        categories = ['Progress', 'Trailer', 'Retriever', 'Excluded']
        heights = [progress, trailer, retriever, excluded]
        colors = ["red", "blue", "green", "pink"]

        # find the max height from the heights
        maxHeight = 0
        for i in heights:
            if i > maxHeight:
                maxHeight = i

        # Drawing the line at the bottom
        line = Line(Point(50, win.getHeight() - 100), Point(win.getWidth() - 50, win.getHeight() - 100)).draw(win)

        # Display other
        position = 0
        barWidth = 90
        for category in categories:

            # Calculate the scaling factor,Scale the height of the bar
            scalor = (win.getHeight() - 200) / maxHeight
            barHeight = heights[position] * scalor

            # no on top of the bars
            barTopCount = Text(Point(barWidth + 70, win.getHeight()  - 100 - barHeight - 20 ), heights[position])
            barTopCount.draw(win)
            barTopCount.setSize(20)
            barTopCount.setTextColor("grey")
            barTopCount.setStyle("bold")

            # boxes
            bar = Rectangle(Point(barWidth, win.getHeight() - 100), Point(barWidth + 140, win.getHeight() - 100 - barHeight))
            bar.setFill(colors[position])
            bar.draw(win)

            #Text under the bars
            catText = Text(Point(barWidth+70,win.getHeight()-80),category)
            catText.setSize(20)
            catText.setTextColor("grey")
            catText.draw(win)


            barWidth += 160
            position +=1

        # Text under the line (Total)
        total_count = progress + trailer + excluded + retriever
        underTxt = f"{total_count} outcomes in total."
        underTxt = Text(Point(250, win.getHeight() - 40), underTxt)
        underTxt.draw(win)
        underTxt.setSize(26)
        underTxt.setStyle("bold")
        underTxt.setTextColor("grey")
        win.getMouse()
        win.close()
    except GraphicsError:
        print("Error creating the histogram window.")



records = []
while True:
    position = input("Are you student or staff ? ").lower()
    if position not in ['student','staff']:
        print('Please enter a valid choice ("student" or "staff").')
    else:
        main()
        break

histogram(progressCount, trailerCount,retrieverCount, excludedCount)

print('part 2')
for record in records:
    print(record)


