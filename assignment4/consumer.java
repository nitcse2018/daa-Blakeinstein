package assignment4;

import java.util.LinkedList;
import java.util.Random;

public class consumer {
    static public class producerConsumer{
        static Random generator = new Random();
        LinkedList<Integer> queue;
        int capacity;
        producerConsumer(int capactiy){
            this.queue = new LinkedList<Integer>();
            this.capacity = capactiy;
        }
        public void produce() throws InterruptedException{
            int value = generator.nextInt(100);
            while(true){
                synchronized(this){
                    while(this.queue.size() == capacity) wait();
                    System.out.println("Producer produced " + value);
                    queue.add(value);
                    notify();
                    Thread.sleep(1000);
                }
            }
        }
        public void consume() throws InterruptedException{
            while(true){
                synchronized(this){
                    while(this.queue.size() == 0) wait();
                    System.out.println("Consumer consumed "+this.queue.removeFirst());
                    notify();
                    Thread.sleep(1000);
                }
            }
        }
    }
    public static void main(String[] args) throws InterruptedException{
        producerConsumer problem = new producerConsumer(5);
        Thread thread1 = new Thread(new Runnable(){
        
            @Override
            public void run() {
                try{
                    problem.produce();
                }
                catch (Exception e){
                    e.printStackTrace();
                }
            }
        });
        Thread thread2 = new Thread(new Runnable(){
        
            @Override
            public void run() {
                try{
                    problem.consume();
                }
                catch (Exception e){
                    e.printStackTrace();
                }
            }
        });
        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();
    }
}