
def main():
  for i in range(5):
      for j in range(5):
          if j == 4:
              print('(' + str(j) + ',' + str(i) + ')')
          else:
              print('(' + str(j) + ',' + str(i) + ')', end=',')





if __name__ == '__main__':
    main()
