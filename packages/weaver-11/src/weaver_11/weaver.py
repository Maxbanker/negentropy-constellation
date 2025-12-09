i
m
p
o
r
t
 
j
s
o
n
,
 
r
e
,
 
n
u
m
p
y
 
a
s
 
n
p


f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
L
i
s
t
,
 
T
u
p
l
e
,
 
D
i
c
t




d
e
f
 
_
s
e
n
t
e
n
c
e
s
(
t
e
x
t
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
p
a
r
t
s
 
=
 
r
e
.
s
p
l
i
t
(
r
'
(
?
<
=
[
.
!
?
]
)
\
s
+
'
,
 
t
e
x
t
.
s
t
r
i
p
(
)
)


 
 
 
 
r
e
t
u
r
n
 
[
p
.
s
t
r
i
p
(
)
 
f
o
r
 
p
 
i
n
 
p
a
r
t
s
 
i
f
 
p
.
s
t
r
i
p
(
)
]




d
e
f
 
_
e
m
b
e
d
(
s
e
n
t
:
 
s
t
r
,
 
d
i
m
:
 
i
n
t
 
=
 
1
2
8
)
 
-
>
 
n
p
.
n
d
a
r
r
a
y
:


 
 
 
 
v
 
=
 
n
p
.
z
e
r
o
s
(
d
i
m
,
 
d
t
y
p
e
=
f
l
o
a
t
)


 
 
 
 
f
o
r
 
t
o
k
 
i
n
 
r
e
.
f
i
n
d
a
l
l
(
r
"
\
w
+
"
,
 
s
e
n
t
.
l
o
w
e
r
(
)
)
:


 
 
 
 
 
 
 
 
h
 
=
 
h
a
s
h
(
t
o
k
)
 
%
 
d
i
m


 
 
 
 
 
 
 
 
v
[
h
]
 
+
=
 
1
.
0


 
 
 
 
n
 
=
 
n
p
.
l
i
n
a
l
g
.
n
o
r
m
(
v
)


 
 
 
 
r
e
t
u
r
n
 
v
 
i
f
 
n
 
=
=
 
0
 
e
l
s
e
 
v
 
/
 
(
n
 
+
 
1
e
-
1
2
)




d
e
f
 
_
c
o
s
i
n
e
(
a
:
 
n
p
.
n
d
a
r
r
a
y
,
 
b
:
 
n
p
.
n
d
a
r
r
a
y
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
n
a
 
=
 
n
p
.
l
i
n
a
l
g
.
n
o
r
m
(
a
)
;
 
n
b
 
=
 
n
p
.
l
i
n
a
l
g
.
n
o
r
m
(
b
)


 
 
 
 
i
f
 
n
a
 
=
=
 
0
 
o
r
 
n
b
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
0
.
0


 
 
 
 
r
e
t
u
r
n
 
f
l
o
a
t
(
n
p
.
d
o
t
(
a
,
 
b
)
 
/
 
(
n
a
*
n
b
 
+
 
1
e
-
1
2
)
)




d
e
f
 
c
o
m
p
u
t
e
_
w
e
f
f
(
s
e
n
t
s
:
 
L
i
s
t
[
s
t
r
]
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
i
f
 
l
e
n
(
s
e
n
t
s
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
1
.
0


 
 
 
 
e
m
b
s
 
=
 
[
_
e
m
b
e
d
(
s
)
 
f
o
r
 
s
 
i
n
 
s
e
n
t
s
]


 
 
 
 
s
i
m
s
 
=
 
[
_
c
o
s
i
n
e
(
e
m
b
s
[
i
]
,
 
e
m
b
s
[
i
+
1
]
)
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
e
m
b
s
)
-
1
)
]


 
 
 
 
j
u
m
p
s
 
=
 
[
1
.
0
 
-
 
s
 
f
o
r
 
s
 
i
n
 
s
i
m
s
]


 
 
 
 
r
e
t
u
r
n
 
f
l
o
a
t
(
1
.
0
 
-
 
n
p
.
m
e
a
n
(
j
u
m
p
s
)
)




d
e
f
 
d
e
t
e
c
t
_
t
e
a
r
s
(
s
e
n
t
s
:
 
L
i
s
t
[
s
t
r
]
,
 
t
h
r
e
s
h
o
l
d
:
 
f
l
o
a
t
 
=
 
0
.
3
5
)
 
-
>
 
L
i
s
t
[
i
n
t
]
:


 
 
 
 
i
f
 
l
e
n
(
s
e
n
t
s
)
 
<
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
[
]


 
 
 
 
e
m
b
s
 
=
 
[
_
e
m
b
e
d
(
s
)
 
f
o
r
 
s
 
i
n
 
s
e
n
t
s
]


 
 
 
 
t
e
a
r
s
 
=
 
[
]


 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
e
m
b
s
)
-
1
)
:


 
 
 
 
 
 
 
 
s
i
m
 
=
 
_
c
o
s
i
n
e
(
e
m
b
s
[
i
]
,
 
e
m
b
s
[
i
+
1
]
)


 
 
 
 
 
 
 
 
i
f
 
1
.
0
 
-
 
s
i
m
 
>
 
t
h
r
e
s
h
o
l
d
:


 
 
 
 
 
 
 
 
 
 
 
 
t
e
a
r
s
.
a
p
p
e
n
d
(
i
)


 
 
 
 
r
e
t
u
r
n
 
t
e
a
r
s




_
P
A
L
E
T
T
E
 
=
 
[


 
 
 
 
"
B
u
i
l
d
i
n
g
 
o
n
 
t
h
a
t
,
 
{
n
e
x
t
}
"
,


 
 
 
 
"
T
o
 
c
o
n
n
e
c
t
 
t
h
i
s
 
i
d
e
a
:
 
{
n
e
x
t
}
"
,


 
 
 
 
"
F
o
l
l
o
w
i
n
g
 
f
r
o
m
 
t
h
e
 
p
r
e
v
i
o
u
s
 
p
o
i
n
t
,
 
{
n
e
x
t
}
"
,


 
 
 
 
"
T
h
i
s
 
n
a
t
u
r
a
l
l
y
 
l
e
a
d
s
 
t
o
:
 
{
n
e
x
t
}
"
,


 
 
 
 
"
I
n
 
l
i
g
h
t
 
o
f
 
t
h
e
 
p
r
i
o
r
 
c
o
n
t
e
x
t
,
 
{
n
e
x
t
}
"
,


 
 
 
 
"
L
e
t
 
m
e
 
l
i
n
k
 
t
h
e
 
e
a
r
l
i
e
r
 
p
o
i
n
t
 
t
o
 
t
h
i
s
:
 
{
p
r
e
v
}
 
→
 
{
n
e
x
t
}
"
,


 
 
 
 
"
B
e
f
o
r
e
 
s
h
i
f
t
i
n
g
,
 
r
e
c
a
l
l
:
 
{
p
r
e
v
}
.
 
N
o
w
,
 
{
n
e
x
t
}
"
,


]




d
e
f
 
a
p
p
l
y
_
b
r
i
d
g
e
s
(
s
e
n
t
s
:
 
L
i
s
t
[
s
t
r
]
,
 
t
e
a
r
s
:
 
L
i
s
t
[
i
n
t
]
)
 
-
>
 
T
u
p
l
e
[
L
i
s
t
[
s
t
r
]
,
 
D
i
c
t
[
i
n
t
,
 
s
t
r
]
]
:


 
 
 
 
i
n
s
e
r
t
e
d
 
=
 
{
}


 
 
 
 
o
f
f
s
e
t
 
=
 
0


 
 
 
 
o
u
t
 
=
 
s
e
n
t
s
[
:
]


 
 
 
 
i
f
 
l
e
n
(
_
P
A
L
E
T
T
E
)
 
=
=
 
0
:


 
 
 
 
 
 
 
 
r
a
i
s
e
 
V
a
l
u
e
E
r
r
o
r
(
"
B
r
i
d
g
e
 
p
a
l
e
t
t
e
 
i
s
 
e
m
p
t
y
;
 
c
a
n
n
o
t
 
r
e
p
a
i
r
 
d
i
a
l
o
g
u
e
.
"
)


 
 
 
 
f
o
r
 
l
o
c
a
l
_
i
d
x
,
 
i
d
x
 
i
n
 
e
n
u
m
e
r
a
t
e
(
t
e
a
r
s
)
:


 
 
 
 
 
 
 
 
i
 
=
 
i
d
x
 
+
 
1
 
+
 
o
f
f
s
e
t


 
 
 
 
 
 
 
 
p
r
e
v
 
=
 
o
u
t
[
i
-
1
]
 
i
f
 
i
-
1
 
>
=
 
0
 
e
l
s
e
 
"
"


 
 
 
 
 
 
 
 
n
x
t
 
=
 
o
u
t
[
i
]
 
i
f
 
i
 
<
 
l
e
n
(
o
u
t
)
 
e
l
s
e
 
"
"


 
 
 
 
 
 
 
 
t
p
l
 
=
 
_
P
A
L
E
T
T
E
[
(
l
o
c
a
l
_
i
d
x
)
 
%
 
l
e
n
(
_
P
A
L
E
T
T
E
)
]


 
 
 
 
 
 
 
 
b
r
i
d
g
e
 
=
 
t
p
l
.
f
o
r
m
a
t
(
p
r
e
v
=
p
r
e
v
,
 
n
e
x
t
=
n
x
t
)


 
 
 
 
 
 
 
 
o
u
t
.
i
n
s
e
r
t
(
i
,
 
b
r
i
d
g
e
)


 
 
 
 
 
 
 
 
i
n
s
e
r
t
e
d
[
i
]
 
=
 
b
r
i
d
g
e


 
 
 
 
 
 
 
 
o
f
f
s
e
t
 
+
=
 
1


 
 
 
 
r
e
t
u
r
n
 
o
u
t
,
 
i
n
s
e
r
t
e
d




d
e
f
 
r
e
p
a
i
r
_
d
i
a
l
o
g
u
e
(
t
e
x
t
:
 
s
t
r
,
 
t
h
r
e
s
h
o
l
d
:
 
f
l
o
a
t
 
=
 
0
.
3
5
)
 
-
>
 
D
i
c
t
:


 
 
 
 
s
e
n
t
s
 
=
 
_
s
e
n
t
e
n
c
e
s
(
t
e
x
t
)


 
 
 
 
w
e
f
f
_
b
e
f
o
r
e
 
=
 
c
o
m
p
u
t
e
_
w
e
f
f
(
s
e
n
t
s
)


 
 
 
 
t
e
a
r
s
 
=
 
d
e
t
e
c
t
_
t
e
a
r
s
(
s
e
n
t
s
,
 
t
h
r
e
s
h
o
l
d
=
t
h
r
e
s
h
o
l
d
)


 
 
 
 
p
a
t
c
h
e
d
_
s
e
n
t
s
,
 
i
n
s
e
r
t
e
d
 
=
 
a
p
p
l
y
_
b
r
i
d
g
e
s
(
s
e
n
t
s
,
 
t
e
a
r
s
)


 
 
 
 
w
e
f
f
_
a
f
t
e
r
 
=
 
c
o
m
p
u
t
e
_
w
e
f
f
(
p
a
t
c
h
e
d
_
s
e
n
t
s
)


 
 
 
 
r
e
t
u
r
n
 
{


 
 
 
 
 
 
 
 
"
t
e
a
r
s
"
:
 
t
e
a
r
s
,


 
 
 
 
 
 
 
 
"
w
e
f
f
_
b
e
f
o
r
e
"
:
 
w
e
f
f
_
b
e
f
o
r
e
,


 
 
 
 
 
 
 
 
"
w
e
f
f
_
a
f
t
e
r
"
:
 
w
e
f
f
_
a
f
t
e
r
,


 
 
 
 
 
 
 
 
"
u
p
l
i
f
t
"
:
 
w
e
f
f
_
a
f
t
e
r
 
-
 
w
e
f
f
_
b
e
f
o
r
e
,


 
 
 
 
 
 
 
 
"
i
n
s
e
r
t
e
d
"
:
 
i
n
s
e
r
t
e
d
,


 
 
 
 
 
 
 
 
"
p
a
t
c
h
e
d
_
t
e
x
t
"
:
 
"
 
"
.
j
o
i
n
(
p
a
t
c
h
e
d
_
s
e
n
t
s
)


 
 
 
 
}


