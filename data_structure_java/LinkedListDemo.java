package data_structure_java;

public class LinkedListDemo{
    public static void main(String args[]){
        LinkedList<String> linkedList = new LinkedList<>();
        System.out.println("(1) 공백 리스트에 노드 3개 삽입하기");
        linkedList.insertLastNode("월");
        linkedList.insertLastNode("수");
        linkedList.insertLastNode("일");
        linkedList.printList();
 
        System.out.println("(2) 수 노드 뒤에 금 노드 삽입하기");
        ListNode<String> pre = linkedList.searchNode("수");
        if(pre == null) 
            System.out.println("검색실패>> 찾는 데이터가 없습니다.");
        else{
            linkedList.insertMiddleNode(pre, "금");
            linkedList.printList();
        }
 
        System.out.println("(3) 리스트의 노드를 역순으로 바꾸기");
        linkedList.reverseList();
        linkedList.printList();
 
        System.out.println("(4) 리스트의 마지막 노드 삭제하기");      
        linkedList.deleteLastNode();
        linkedList.printList();
    }
}
 
class LinkedList<T>{
    private ListNode<T> head;
    public LinkedList(){
        head = null;
    }
    //지정한 노드 뒤에 삽입
    public void insertMiddleNode(ListNode<T> pre, T data){       
        ListNode<T> newNode = new ListNode<>(data);
        newNode.link = pre.link; // pre.link는 pro의 다음 노드이므로 새로운 노드의 링크가 pre의 다음 노드를 참조
        pre.link = newNode;      // pre.link가 다음 노드를 참조
    }
    // 마지막에 노드 삽입
    public void insertLastNode(T data){
        ListNode<T> newNode = new ListNode<>(data);
        if(head == null){
            this.head = newNode; // 헤드가 참조하는 노드가 없는 경우 == 빈 자료구조일 경우 
        }
        else{
            ListNode<T> temp = head;  // 마지막 노드를 찾아서 참조하기 위한 임시 변수
            while(temp.link != null){ // 마지막 노드를 찾을 때까지 반복한다.
                temp = temp.link; 
            }
            temp.link = newNode;      // 마지막 링크에 노드를 삽입한다.
        }
    }
    // 마지막 노드 삭제
    public void deleteLastNode(){
        ListNode<T> pre;
        ListNode<T> temp;
        if(head == null) {
            return;
        }
        if(head.link == null){
            head = null;
        }
        else{
            pre = head;
            temp = head.link;
            while(temp.link != null){
                pre = temp;
                temp = temp.link;
            }
            pre.link = null;
        }
    }
    public ListNode<T> searchNode(T data){
        ListNode<T> temp = this.head;
        while(temp != null){
            if(data == temp.getData())  
                return temp;
            else temp = temp.link;
        }
        return  temp;
    }
    public void reverseList(){
        ListNode<T> next = head;
        ListNode<T> current = null;
        ListNode<T> pre = null;
        while(next != null){
            pre = current;
            current = next;
            next = next.link;
            current.link = pre;
        }
        head = current;
    }
    public void printList(){
        ListNode<T> temp = this.head;
        System.out.printf("L = (");
        while(temp != null){
            System.out.printf(temp.getData().toString());
            temp = temp.link;
            if(temp != null){
                System.out.printf(", ");
            }            
        }
        System.out.println(")");
    }
}
 
class ListNode<T>{
    private T data;
    public ListNode<T> link;
    public ListNode(){
        this.data = null;
        this.link = null;
    }
    public ListNode(T data){
        this.data = data;
        this.link = null;
    }
    public ListNode(T data, ListNode<T> link){
        this.data = data;
        this.link = link;
    }
    public T getData(){
        return  this.data;
    }
    public ListNode<T> getHead(){
        return this.link;
    }
    public int getAddress(){
        return System.identityHashCode(this);
    }
}

