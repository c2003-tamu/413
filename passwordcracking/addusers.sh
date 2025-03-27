useradd -m -s /bin/bash "user1"
echo "user1:4056" | chpasswd -c MD5

useradd -m -s /bin/bash "user2"
echo "user2:34867" | chpasswd -c MD5

useradd -m -s /bin/bash "user3"
echo "user3:598212" | chpasswd -c MD5

useradd -m -s /bin/bash "user4"
echo "user4:7728694" | chpasswd -c MD5

useradd -m -s /bin/bash "user5"
echo "user5:13063382" | chpasswd -c MD5
