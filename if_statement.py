#if statement
ph = float(input('Enter thr pH level: '));
if ph < 7.0:
    print(ph,"is acidic");
    print("Be careful with that");
elif ph > 7.0:
    print(ph,"is basic"); #elif는 if문이 false일 때만 연산진행

#using boolean variable
young = age <45
slim = bmi <22.0
if young:
    if slim:
        risk = "low";
    else:
        risk = "medium";
else:
    if slim:
        risk = "medium";
    else:
        risk = "high";
