# 开发技巧

## JSON
### Gson
* [开源地址](https://github.com/google/gson)

常用方法:
```java
import com.google.gson.Gson;
public class JSON {
    private static Gson g = new Gson();
    public static String Serializer(Object obj) {
        return g.toJson(obj);
    }
    public static <T> T Deserialize(String str, Class<T> c) {
        try {
            return g.fromJson(str, c);
        } catch (Exception e) {
            return null;
        }
    }
}
```
