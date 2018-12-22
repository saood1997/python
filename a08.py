## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(markList):
  if markList == None:
    return None
  elif len(markList) == 0:
    return []
  else:
    cumulativeList = []
    for student in markList:
      currentStudentAggr = 0
      for mark in student[2:]:
        if mark:
          currentStudentAggr += mark
      cumulativeList.append((student[0], student[1], currentStudentAggr))
    return cumulativeList
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
  if results == None:
    return None
  elif len(results) == 0:
    return []
  else:
    cumulativeList = []
    for student in results:
      currentStudentAggr = 0
      for mark in student[2:]:
        if mark:
          currentStudentAggr += mark
      cumulativeList.append((student[0], student[1]))
      cumulativeList.sort(reverse=True)
	
    return cumulativeList[0]
		
#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
