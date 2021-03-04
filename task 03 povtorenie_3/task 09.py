nums = [15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5]

print({num: "> 0" if num > 0 else "< 0" if num < 0 else "= 0" for num in nums})
