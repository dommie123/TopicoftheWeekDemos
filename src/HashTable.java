import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.LinkedList;

public class HashTable {
	
	private Map<Integer, LinkedList<String>> data; // I can confirm that I maintain space complexity of O(n) by using a Map to house the data.
	private int size;
	private int capacity;
	
	public HashTable(int capacity) {
		this.capacity = capacity;
		this.size = 0;
		this.data = new HashMap<Integer, LinkedList<String>>();
	}
	
	public HashTable() {
		this(10);
	}
	
	public String get(int index) {
		if (data.isEmpty()) return null;
		return data.get(index).getFirst();
	}
	
	public String get(int i1, int i2) {
		if (data.isEmpty()) return null;
		return  data.get(i1).get(i2);
	}
	
	public void insert(String str) {
		int key = hash(str);
		if (!data.containsKey(key)) {
			data.put(key, new LinkedList<String>());
		}
		data.get(key).add(str);
		size++;
		if (capacity == size) capacity *= 2;
	}
	
	public void delete(String str) {
		int key = hash(str);
		for (int i = 0; i < data.get(key).size(); i++) {
			if (str == data.get(key).get(i)) {
				data.get(key).remove(i);
			}
		}
	}
	
	public void delete(String str, int index) {
		int key = hash(str);
		data.get(key).remove(index);
		size--;
		if (size <= Math.floorDiv(capacity, 4)) capacity /= 2;
	}
	
	// First attempt at coding a hash function. 
	private int hash(String str) {
		return Math.abs(str.hashCode() % capacity);
	}
	
	@Override
	public String toString() {
		return data.toString();
	}
}
