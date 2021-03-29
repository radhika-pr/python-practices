#Find no: of seats per family(of 4) in a flight
#input Number of seats N and reserved seats array S
#The seats are numbered with alphabets from A to K excluding I
#Eg: Seats in first row - 1A,1B,1C, 1D,1E,1F,1G, 1H,1J,1K
# Family of 4 need to be seated adjacent to each other eg: possible seats are B,C,D,E or D,E,F,G or F,G,H,J
#Find number of seats available for a family in given flight
#Input example : solution(2,['1B', '1C','1H', '2K']) return 3

from string import ascii_uppercase
def solution(N,S):
    #check if booked seats array is empty. Then return 2 seats/family in each row
    if not S:
        return N*2
    #Find total seats numbered
    all_seats = findAllSeats(N)
    #cross check total seats against reserved and mark available seat position as "Green"
    available_seats = findAvailableSeats(all_seats,S,N)
    no_seats =0
    #Find number of seats for family by checking the possibility of seating
    no_seats = findSeatCount(available_seats,N)
    return no_seats

 #Function to find all seats with given number of rows
def findAllSeats(rows):
    seats = [i for i in ascii_uppercase if i!='I']
    all_seats=[]
    for i in(0,rows-1):
        rows=[]
        for c in (seats[:10]):
            rows.append(str(i+1)+c)
        all_seats.append(rows)
    return all_seats

#Function to find available seats cross checked against reserved seats and mark them as Green
def findAvailableSeats(all_seats,reserved,rows):
    available=[]
    for i in (0,rows-1):
        A = [j if j in reserved else "GREEN" for j in all_seats[i]]
        available.append(A)
    return available

#Count available seats for families
def findSeatCount(available_seats,rows):
    seat_count =0
    for i in (0,rows-1):
        #If B-J is all Green then 2 families can be seated
        if all(seat == 'GREEN' for seat in available_seats[i][1:9] ):
            seat_count=seat_count+2
            continue
        #If B-E is green
        if all(seat == 'GREEN' for seat in available_seats[i][1:5] ):
            seat_count=seat_count+1
        #If F-J is green
        if all(seat == 'GREEN' for seat in available_seats[i][5:9] ):
            seat_count=seat_count+1
         #If D-G is green
        if all(seat == 'GREEN' for seat in available_seats[i][3:7] ):
            seat_count=seat_count+1
    return seat_count
