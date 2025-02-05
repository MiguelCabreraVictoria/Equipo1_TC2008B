using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class PythonSocketClient : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private byte[] receivedBuffer = new byte[1024];

    void Start()
    {
        ConnectToServer();
    }

    void Update()
    {
        if (client != null && client.Connected)
        {
            ReceiveData();
        }
    }

    void ConnectToServer()
    {
        try
        {
            client = new TcpClient("127.0.0.1", 65432);  // Asegúrate de que el puerto coincide con el de Python
            stream = client.GetStream();
            Debug.Log("Connected to Python server!");
        }
        catch (Exception e)
        {
            Debug.LogError($"Connection error: {e.Message}");
        }
    }

    void ReceiveData()
    {
        if (stream.DataAvailable)
        {
            int bytesRead = stream.Read(receivedBuffer, 0, receivedBuffer.Length);
            string dataReceived = Encoding.UTF8.GetString(receivedBuffer, 0, bytesRead);

            Debug.Log($"Data received: {dataReceived}");

            // Aquí puedes parsear los datos y actualizar los objetos en Unity
            ProcessData(dataReceived);
        }
    }

    void ProcessData(string data)
    {
        // Parsear el JSON recibido
        var state = JsonUtility.FromJson<StateData>(data);

        // Actualiza la posición de los coches y peatones en Unity aquí
        // Ejemplo: Actualizar posiciones de los objetos con los IDs correspondientes
    }

    private void OnApplicationQuit()
    {
        if (stream != null)
            stream.Close();
        if (client != null)
            client.Close();
    }
}

[Serializable]
public class StateData
{
    public Vector2[] cars;
    public Vector2[] pedestrians;
}
