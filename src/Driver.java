
public class Driver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashTable htable = new HashTable(50);
		htable.insert("Bob");
		htable.insert("Joe");
		htable.insert("Clyde");
		htable.insert("Doge");
		htable.insert("Coin");
		htable.insert("Is");
		htable.insert("Best");
		htable.insert("Crypto");
		htable.insert("Currency");
		htable.insert("Beep");
		System.out.println(htable);
		htable.delete("Clyde");
		htable.delete("Joe");
		htable.delete("Bob");
		htable.delete("Is");
		htable.delete("Beep");
		htable.delete("Coin");
		System.out.println(htable);
		System.out.println(htable.get(3));
		System.out.println(htable.get(29));
	}
}
