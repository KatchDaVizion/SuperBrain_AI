import React, { useState } from 'react';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Loader2 } from 'lucide-react';

export default function MultiModel() {
  const [prompt, setPrompt] = useState('');
  const [responses, setResponses] = useState({});
  const [loading, setLoading] = useState(false);

  const models = [
    { id: 'openai', name: 'OpenAI' },
    { id: 'claude', name: 'Claude' },
    { id: 'gemini', name: 'Gemini' },
    { id: 'groq', name: 'Groq' },
    { id: 'venice', name: 'Venice' }
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    setLoading(true);
    const newResponses = {};

    try {
      // Query each model in parallel
      await Promise.all(models.map(async (model) => {
        try {
          const response = await fetch(`/api/${model.id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
          });
          
          if (!response.ok) throw new Error(`${model.name} API error`);
          const data = await response.json();
          newResponses[model.id] = data.response;
        } catch (error) {
          newResponses[model.id] = `Error: ${error.message}`;
        }
      }));

      setResponses(newResponses);
    } catch (error) {
      console.error('Error querying models:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-6 max-w-6xl">
      <h1 className="text-3xl font-bold mb-6">Multi-Model Query</h1>
      
      <form onSubmit={handleSubmit} className="mb-6">
        <Textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here..."
          className="mb-4"
          rows={4}
        />
        <Button type="submit" disabled={loading || !prompt.trim()}>
          {loading ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Querying Models...
            </>
          ) : (
            'Query All Models'
          )}
        </Button>
      </form>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {models.map((model) => (
          <Card key={model.id} className="w-full">
            <CardHeader className="pb-3">
              <h2 className="text-xl font-semibold">{model.name}</h2>
            </CardHeader>
            <CardContent>
              <ScrollArea className="h-[200px] w-full rounded-md border p-4">
                {loading ? (
                  <div className="flex items-center justify-center h-full">
                    <Loader2 className="h-6 w-6 animate-spin" />
                  </div>
                ) : responses[model.id] ? (
                  <p className="whitespace-pre-wrap">{responses[model.id]}</p>
                ) : (
                  <p className="text-muted-foreground">No response yet</p>
                )}
              </ScrollArea>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}