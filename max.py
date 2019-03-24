def find_max(num):
    max = num[0]
    for x in num:
      if x > max:
        max = x
    print(max)

def main():
  find_max([8, 10, 4, 26, 65, 94, 5])

if __name__ == '__main__':
  main()
