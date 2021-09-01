#include <ros.h>
#include <std_msgs/String.h>

ros::nodeHandle nh;
std_msgs::String str_msg;

ros::Publisher chatter('chatter', &str_msg);

char word[13]= "Hello World!";

void setup()
{
  nh.initNode();
  nh.advertise(chatter)
}

void loop()
{
  str_msg.data = word;
  chatter.publish( &str_msg);
  nh.spinOnce();
  delay(1000);
}
