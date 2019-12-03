import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Memory } from '../models';

@Injectable({
  providedIn: 'root'
})
export class MemoryService {

  constructor(private storage: Storage) {
    this.getMemories().then(data =>
      {
        if (!data) {
          this.storage.set('memories', [])
        }
      })
  }

  addMemories(memory: Memory) {
    return this.getMemories().then(data => {
      data.push(memory)
      return this.storage.set('memories', data)
    }).catch(err => {
      console.log('Error Add Memory')
      console.log(memory)
      console.log(err)
    })
  }

  getMemories(): Promise<any> {
    return this.storage.get('memories')
  }

  private generateMemories(count: Number) {
    var memories = []
    for (var i = 0; i < count; i++) {
      memories.push(this.generateMemory())
    }
    return memories
  }

  private generateMemory(): Memory {
    return {
      Title: "Bushido",
      Type: "Journal",
      PageStart: 5,
      PageEnd: 60,
      Tags: [],
      ContentList: [{
        Title: 'Example One',
        Body: 'This is some common description or record',
        Attachments: [],
        Tags: []
      }],
      DateCreated: new Date()
    }
  }
}
