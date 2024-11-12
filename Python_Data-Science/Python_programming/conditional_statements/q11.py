#Nested if
#type 1
 #
#  if cond1:
 #     stmt 1
 # else:
 #     if cond2:
 #         stmt2
 #     else:
 #         stmt3
 #
 #         type 2
 #
#
#         if cond1:
 #             if cond2:
 #                 stmt1
 #             else:
 #                 stmt2
 #         else:
 #            stmt3

 #
 # type3
 # if cond1:
 #     if cond2:
 #         stmt 1
 #     else:
 #         stmt2
 # else:
 #     if cond3:
 #         stmt3
 #     else:
 #         stmt4
 #
n=int(input("Enter the number:"))
if n>=0:
    if n>0:
     print("positive")
    else:
     print("Zero")
else:
  print("Negative")
