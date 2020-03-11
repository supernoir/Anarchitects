import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, SafeAreaView, SectionList, Button, TextInput } from 'react-native';

type Building = { id: string, name: string, value: number }

export default function App() {

  const [buildings, setBuildings] = useState([])
  const [buildingName, setBuildingName] = useState("")

  useEffect(() => {
    getBuildings()
    setBuildings(mockBuildings)
  }, [])

  function handleBuildingNameInput(name: string) {
    setBuildingName(name)
  }

  const mockBuildings = [
    {
      title: "Feracious Fields",
      data: [{
        id: 22,
        name: "Feracious Fields",
        value: 10244.19
      }]
    },
    {
      title: "Greene Meadows",
      data: [{
        id: 14,
        name: "Greene Meadows",
        value: 1989.11
      }]
    },
    {
      title: "Woodlawn Terrace",
      data: [{
        id: 14,
        name: "Woodlawn Terrace",
        value: 23232.10
      }]
    },
    {
      title: "Mohawk Estates",
      data: [{
        id: 16,
        name: "Mohawk Estates",
        value: 23232.10
      }]
    },
  ]

  function getBuildings() {
    return fetch('http://192.168.178.33:5000/buildings', {
      mode: 'cors',
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then((response) => {
        return response.json()
      })
      .then(responseJson => {
        const buildingsData = responseJson && responseJson.buildings.map((item) => {
          return { title: item.name, value: item.value, data: [item] }
        });
        setBuildings(buildingsData)
      })
      .catch((error) => {
        console.error(error);
      });
  }

  function createNewBuilding() {
    return {
      name: buildingName, value: 0
    }
  }

  function triggerAddBuilding() {
    const data = createNewBuilding()
    return fetch('http://192.168.178.33:5000/buildings', {
      method: 'POST',
      mode: 'cors',
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      },
      body: JSON.stringify(data)
    })
      .then((response) => {
        return response.json()
      })
      .then(responseJson => {
        console.log(responseJson)
      })
      .catch((error) => {
        console.error(error);
      });
  }

  function Item({ title, value }) {
    return (
      <View style={styles.item}>
        <Text>{title}</Text>
        <Text>{value}</Text>
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View>
        <SectionList
          sections={buildings}
          keyExtractor={(item: { title: string, value: number }, index: number) => item.title + index}
          renderItem={({ item }) => <Item title={item.title} value={item.value} />}
          renderSectionHeader={({ section: { title } }) => <Text style={styles.header}>{title}</Text>}
        />
      </View>
      <View>
        <Text>{buildingName}</Text>
        <TextInput
          style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
          onChangeText={text => handleBuildingNameInput(text)}
          value={buildingName}
        />
        <Button
          title="Add Building"
          onPress={triggerAddBuilding}
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    //marginHorizontal: 16,
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
  },
  header: {
    fontSize: 32,
  },
  title: {
    fontSize: 24,
  },
});
